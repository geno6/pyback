local:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - django
    - settings
    - superuser
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
    - cron