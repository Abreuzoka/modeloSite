"""
WSGI config for modeloSite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

path = 'C:\\Users\\Gabriel\\Downloads\\modeloSite'  # use your own PythonAnywhere username here
sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'modeloSite.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())