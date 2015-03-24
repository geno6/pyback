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
    - git
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
    - git
    - gunicorn
    - postgresql
    - venv
    - nginx
    - django
    - settings
    - superuser
    - mongodb
    - cron