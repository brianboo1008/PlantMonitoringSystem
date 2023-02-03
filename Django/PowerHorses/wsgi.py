
import os
import sys

## assuming your django settings file is at '/home/simplicat/mysite/mysite/settings.py'
## and your manage.py is is at '/home/simplicat/mysite/manage.py'
path = '/home/boospammer999/PlantMonitoringSystem/PowerHorses'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'PowerHorses.settings'

## then, for django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
## or, for older django <=1.4
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
