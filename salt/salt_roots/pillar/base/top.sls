local:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - django

dev:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - django

prod:
  '*':
    - gunicorn
    - postgresql
    - venv
    - nginx
    - django