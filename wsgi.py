import os, sys

sys.path.append('/var/www/imobiliaria')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "imobiliaria.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()