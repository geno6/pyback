"""
WSGI config for pyback project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import pymysql

try:
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyback.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
