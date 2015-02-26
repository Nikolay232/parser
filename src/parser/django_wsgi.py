import os
import sys

sys.path.append('/usr/share/pyshared/django')

os.environ['DJANGO_SETTINGS_MODULE'] = 'hrbparserrand.settings'
os.environ['DJANGO_PRODUCTION_SETTINGS_PATH'] = '/etc/parser/settings.py'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
