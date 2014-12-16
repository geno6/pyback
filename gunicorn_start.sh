#!/bin/bash

NAME="pyback"                              #Name of the application (*)
DJANGODIR=/var/www             # Django project directory (*)
USER=vagrant                                        # the user to run as (*)
GROUP=vagrant                                     # the group to run as (*)
NUM_WORKERS=1                                     # how many worker processes should Gunicorn spawn (*)
DJANGO_SETTINGS_MODULE=pyback.settings             # which settings file should Django use (*)
DJANGO_WSGI_MODULE=pyback.wsgi                     # WSGI module name (*)

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
. /var/www/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /var/www/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application   --bind=localhost:12345  --workers $NUM_WORKERS --user $USER \
--name $NAME