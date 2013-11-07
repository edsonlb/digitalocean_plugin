import os
import sys

path = '/var/www/imobiliaria'
if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'imobiliaria.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()