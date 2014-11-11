#!/bin/sh

export DJANGO_SETTINGS_MODULE=pyback.settings.production

python3.4 manage.py runserver 192.168.55.10:8000