postgresql:
  user: root
  password: password
  database: pyback

website:
  venv_dir: /var/www/venv
  venv_activate_path: /var/www/venv/bin/activate
  settings_path: /var/www/system/settings.py
  static_dir: /var/www/static/
  src_dir: /var/www
  requirements_path: /var/www/requirements.txt