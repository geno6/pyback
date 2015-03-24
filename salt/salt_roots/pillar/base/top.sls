local:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - django
    - settings
    - superuser
    - mongodb
    - cron

dev:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - django
    - settings
    - superuser
    - mongodb
    - cron

prod:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - django
    - settings
    - superuser
    - mongodb
    - cron