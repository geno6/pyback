postgresql:
  user: root
  password: password
  database: pyback

website:
  venv_dir: /var/www/venv
  venv_activate_path: /var/www/venv/bin/activate
  settings_path: /var/www/system/settings.py
  static_dir: /var/www/static/
  media_dir: /var/www/media/
  wsgi_file_path: /var/www/system/wsgi.py
  src_dir: /var/www
  requirements_path: /var/www/requirements.txt

uwsgi:
  reload: True
  processes: 3