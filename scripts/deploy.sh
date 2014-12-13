#!/bin/sh
source venv/bin/activate
export DJANGO_SETTINGS_MODULE=pyback.settings
git pull
pip install -r requirements.txt

# Update database, static files, locales
manage.py syncdb  --noinput
manage.py migrate
manage.py collectstatic --noinput
manage.py makemessages -a
manage.py compilemessages

# restart wsgi
touch pyback/wsgi.py