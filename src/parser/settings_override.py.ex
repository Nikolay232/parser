import os
from datetime import datetime, timedelta

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'hhservice',
        'USER': 'hruser',
        'PASSWORD': '1234'
        }
    }

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'noreply@hh.ru'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, '../templates'),
)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../media/')
#MEDIA_ROOT = '/var/www/webdav'
#MEDIA_URL = '/media/'
MEDIA_URL = 'http://localhost:8008/webdav'

STATIC_ROOT = os.path.join(PROJECT_ROOT, '../static/')
STATIC_URL = '/static/'

TINYMCE_JS_URL = '/static/js/tinymce/tiny_mce.js'

handler = { 'class': 'logging.FileHandler', 'filename':
    os.path.join(PROJECT_ROOT, '../parser.log'), 'formatter':
    'verbose' }

email_handler = { 'class': 'logging.FileHandler', 'filename':
    os.path.join(PROJECT_ROOT, '../emails.log'), 'formatter':
    'verbose' }


STREAM_START = datetime.now() - timedelta(hours=10)
STREAM_FINISH = datetime.now() + timedelta(hours=5)
STREAM_PAGE_URL = '/live/'

UPLOAD_TYPE_DOCUMENT = [ 'application/pdf', 'application/msword',
                        'application/excel', 'text/plain',
                        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                        ]
UPLOAD_TYPE_IMAGE = [ 'image/png',
                      'image/jpeg',
                      'image/gif',
                      ]
UPLOAD_TYPE_OTHER = [
    'application/zip'
    ]

RATING_REGISTRATION_OPEN = True
RATING_POLL_OPEN = True

UPLOAD_PUT_URL = 'http://localhost:8008/webdav/'
UPLOAD_TIMEOUT = 100
PING_FILENAME = 'pingfile'

DEFAULT_FILE_STORAGE = 'parser.webdav.storage.WebDavUploader'
