# -*- coding: utf-8 -*-
import os
import sys
import datetime
from parser import package_version

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'parser_bd',
        'USER': 'parser_user',
        'PASSWORD': '1234'
    }
}

PACKAGE_VERSION = package_version

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Nikolay Kotov', 'mikola1717@gmail.com'),
)

MANAGERS = ADMINS

SITE_ID = 1

LOGIN_URL = '/'

CURRENT_YEAR = datetime.datetime.now().year

GA_CODES = {}

LI_CODES = {}

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'
DATE_FORMAT = 'd.m.Y'
USE_I18N = True
USE_L10N = True

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

SECRET_KEY = 'o%-_m$n5w4a$#t)%l9lb1-pfp5y3jni1ci&173yh%)cl)^5@pb'
CSRF_MIDDLEWARE_SECRET = '70213b451c07e0c3c460b3ed6a325356'

ROOT_URLCONF = 'parser.urls'

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'parser.webdav'

)

TEMPLATE_CONTEXT_PROCESSORS = (
    # default template context processors
    "django.contrib.auth.context_processors.auth",
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    # required by django-admin-tools
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)

ADMIN_TOOLS_INDEX_DASHBOARD = 'parser.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_MENU = 'parser.menu.CustomMenu'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/projects/'
ACCOUNT_ACTIVATION_DAYS = 2

MAX_HHID = 2147483647

CONFIG_PATH = '/etc/parser/'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'noreply@hh.ru'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../media/')
MEDIA_URL = 'http://localhost:8008/webdav/'

STATIC_URL = '/static/'

AUDIT_URL = '/audit/'

handler = {'class': 'logging.FileHandler', 'filename':
           os.path.join(PROJECT_ROOT, '../parser.log'), 'formatter':
           'verbose'}

email_handler = {'class': 'logging.FileHandler', 'filename':
                 os.path.join(PROJECT_ROOT, '../emails.log'), 'formatter':
                 'verbose'}

UPLOAD_TYPE_DOCUMENT = ['application/pdf', 'application/msword',
                        'application/excel', 'text/plain',
                        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                        ]
UPLOAD_TYPE_IMAGE = ['image/png',
                     'image/jpeg',
                     'image/gif',
                     ]
UPLOAD_TYPE_OTHER = [
    'application/zip'
]

PROFILE_RESEARCH_UPLOAD_TYPE = [
    'text/csv',
    'application/vnd.ms-excel',
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.oasis.opendocument.spreadsheet',
    'application/vnd.sun.xml.calc',
]

PROFILE_RESEARCH_UPLOAD_SIZE = 20971520
MAX_REPORT_UPLOAD_SIZE = 5242880

UPLOAD_PUT_URL = 'http://localhost:8008/webdav/'
UPLOAD_TIMEOUT = 100
UPLOAD_GET_TIMEOUT = 100
PING_FILENAME = '00000.test'

NUMBER_VOICES_CLEAN_PARAMETER = 2

DEFAULT_FILE_STORAGE = 'parser.webdav.storage.WebDavUploader'

FIXTURE_DIRS = (os.path.join(PROJECT_ROOT, '../init'),)

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(module)s %(process)d %(message)s'
        },
    },
    'handlers': {'default': handler,
                 'email': email_handler},
    'loggers': {
        'django': {
            'handlers': ['default'],
            'level': 'DEBUG',
        },
        'parser': {
            'level': 'INFO',
    'handlers': ['default', 'email'],
        },
    }
}

PRODUCTION_SETTINGS_PATH = SETTINGS_OVERRIDE_PATH = os.environ.get('DJANGO_PRODUCTION_SETTINGS_PATH')

#RECAPTCHA_PUBLIC_KEY = '6Lcs5uUSAAAAAPPPeLANEZsMC1-btPprY9UPV6m_'
#RECAPTCHA_PRIVATE_KEY = '6Lcs5uUSAAAAAOXHxI-5_L4tu40uDnGgBVu1Z_e5'

IMAGE_DEFAULT_SIZE = [1920, 1080]
USE_X_FORWARDED_HOST = None

datetime_max = datetime.datetime.max
datetime_min = datetime.datetime.min

if PRODUCTION_SETTINGS_PATH is None:
    DEV_SETTINGS_PATH = os.path.join(PROJECT_ROOT, 'settings_override.py')
    if os.path.exists(DEV_SETTINGS_PATH):
        SETTINGS_OVERRIDE_PATH = DEV_SETTINGS_PATH

if SETTINGS_OVERRIDE_PATH is not None:
    exec open(SETTINGS_OVERRIDE_PATH) in locals()

FIXTURE_DIRS = [os.path.join(PROJECT_ROOT, 'tests/fixtures/')]

if DEBUG and 'test' in sys.argv:
    INSTALLED_APPS += ('inmemorystorage',)
    DEFAULT_FILE_STORAGE = 'inmemorystorage.storage.InMemoryStorage'

    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )

    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/parser-test',
    }
