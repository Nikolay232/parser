# -*- coding: utf-8 -*-
DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'parser_bd',
        'USER': 'parser_user',
        'PASSWORD': '1234'
    }
}

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

MEDIA_ROOT = '/var/www/parser/media'
MEDIA_URL = 'http://webdav.hh.com:80/'

STATIC_URL = 'http://i.parser.ru/'

UPLOAD_TYPE_DOCUMENT = [
    'application/pdf',
    'application/msword',
    'application/vnd.ms-excel',
    'text/plain',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
]

UPLOAD_TYPE_IMAGE = ['image/png', 'image/jpeg', 'image/gif',]
UPLOAD_TYPE_OTHER = ['application/zip',]
PROFILE_RESEARCH_UPLOAD_TYPE = [
    'text/csv',
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.oasis.opendocument.spreadsheet',
    'application/vnd.sun.xml.calc',
]

PROFILE_RESEARCH_UPLOAD_SIZE = 20971520


handler = {'class': 'logging.handlers.WatchedFileHandler',
           'filename': '/var/log/parser/parser.log',
           'level': 'DEBUG',
           'formatter': 'verbose'}

email_handler = {'class': 'logging.handlers.WatchedFileHandler',
                 'filename': '/var/log/parser/emails.log',
                 'level': 'DEBUG',
                 'formatter': 'verbose'}

gelf_handler = {
    'class': 'graypy.GELFHandler',
    'host': 'localhost',
    'port': 10513
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(module)s %(process)d %(message)s'
        },
    },
    'handlers': {
        'default': handler,
        'email': email_handler,
        'gelf': gelf_handler
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'gelf'],
            'level': 'DEBUG',
        },
        'parser': {
            'level': 'INFO',
            'handlers': ['default', 'email', 'gelf'],
        },
    }
}

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
