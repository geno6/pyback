gunicorn:
  cmd: /var/www/venv/bin/gunicorn
  reload: --reload
  workers: 3