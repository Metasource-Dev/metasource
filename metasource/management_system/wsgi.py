import os
import sys

# Add the project directory to the sys.path
project_home = '/home/pfcbmldcyttq/metasource/'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set environment variable for Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'management_system.settings'

# Import and setup Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
