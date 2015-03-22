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