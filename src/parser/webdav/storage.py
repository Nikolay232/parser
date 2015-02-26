# -*- coding: utf-8 -*-
import httplib
import os

from StringIO import StringIO
from datetime import datetime
from httplib import HTTPException
from logging import getLogger
from socket import error as socket_error
from urlparse import urlparse

from django.core.files.base import ContentFile
from django.core.files.storage import Storage

from parser import package_name, package_version, settings
from parser.models import MediaFileSequence


logger = getLogger('parser.storage')


class DisallowedStatus(HTTPException):

    def __init__(self, msg, code, allowed_codes, connection):
        super(DisallowedStatus, self).__init__(msg)
        self.code = code
        self.allowed_codes = allowed_codes
        self.connection = connection


class HTTPClient(object):
    def __init__(self, url, timeout=1000):
        self._host, self._port, self._path = self.__parse_url(url)
        self._connection = httplib.HTTPConnection(self._host, self._port, timeout=float(timeout) / 1000)

    def __parse_url(self, url):
        parsed = urlparse(url)
        return parsed.hostname, parsed.port, parsed.path

    def put(self, name, stream, allowed_statuses=[200, 201, 202, 203, 204, 205, 206, 207]):
        stream.seek(0, 2)
        length = stream.tell()
        stream.seek(0)
        headers = {
            'Content-Length': length,
        }
        return self.request('PUT', os.path.join(self._path, name),
                            stream,
                            headers,
                            allowed_statuses=allowed_statuses)

    def get(self, path, allowed_statuses=[200, ]):
        response = self.request('GET', os.path.join(self._path, path),
                                allowed_statuses=allowed_statuses)
        return response

    def options(self, path):
        return self.request('OPTIONS', os.path.join(self._path, path))

    def request(self, *args, **kwargs):
        connection = kwargs.get('connection', None)
        request_method = args[0]
        request_path = args[1]
        allowed_statuses = kwargs.get('allowed_statuses', None)

        if not connection:
            connection = self._connection

        url = "{host}:{port}{path}".format(host=connection.host, port=connection.port, path=request_path)
        try:
            connection.request(*args)

        except (HTTPException, socket_error), ex:
            logger.error('Error on {method} request to {url}: {message} '.format(
                url=url,
                method=request_method,
                message=str(ex)
            ), exc_info=False)
            raise ex
        else:
            response = connection.getresponse()
            if request_method == 'GET':
                response.body = response.read()
        finally:
            connection.close()

        if allowed_statuses and response.status not in allowed_statuses:
            raise DisallowedStatus('Bad response status {code} on {method} request to url {path}'
                                   .format(code=response.status, method=request_method, path=url),
                                   response.status, allowed_statuses, connection)

        return response


class WebDavUploader(Storage):
    def __init__(self, location=None, base_url=None, put_client=None, get_client=None):

        # We use differend instances of HTTPClient for get and put requests
        if put_client is None:
            put_client = HTTPClient(settings.UPLOAD_PUT_URL, settings.UPLOAD_TIMEOUT)

        if get_client is None:
            get_client = HTTPClient(settings.MEDIA_URL, settings.UPLOAD_GET_TIMEOUT)

        self.put_client = put_client
        self.get_client = get_client

    def upload(self, filename, stream):
        logger.info(filename)
        logger.info('put file {0}'.format(filename))

        self.put_client.put(filename, stream)

    def save(self, name, content):
        file_format = name.split('.')[-1]
        seq_name = '.'.join([MediaFileSequence.get_next(), file_format])
        self.upload(seq_name, content.file)
        return seq_name

    def open(self, filename, mode='rwb'):
        response = self.get_client.get(filename)
        return ContentFile(response.body)

    def url(self, name):
        return os.path.join(settings.MEDIA_URL, name)

    def check_conn(self):
        test_file = StringIO()
        test_file.write('Package: {name}, Version: {version}, Time: {time}\n'
                        .format(name=package_name, version=package_version, time=str(datetime.now())))
        filename = settings.PING_FILENAME
        try:
            put_response = self.put_client.put(filename, test_file)
            get_response = self.get_client.get(filename)

        except (HTTPException, socket_error), ex:
            logger.error('Error on status check of webDAV server on host {dsn}: {msg}'
                         .format(dsn=settings.UPLOAD_PUT_URL, msg=str(ex)),
                         exc_info=False)
            return False

        else:
            return True

    def exists(self, filename):
        try:
            get_response = self.get_client.get(filename, get_url=settings.MEDIA_URL)
        except DisallowedStatus:
            return False
        return True
