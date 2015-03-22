local:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - django
    - settings
    - mongodb

dev:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - settings
    - django
    - mongodb

prod:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - settings
    - django
    - mongodb