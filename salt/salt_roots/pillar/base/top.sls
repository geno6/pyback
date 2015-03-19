local:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - django
    - settings

dev:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - settings
    - django

prod:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - settings
    - django