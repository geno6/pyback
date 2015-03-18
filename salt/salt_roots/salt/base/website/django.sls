{{ pillar['website']['venv_dir'] }}:
  file:
    - directory
    - makedirs: True

  virtualenv:
    - managed
    - no_site_packages: True
    - distribute: True
    - python: /usr/bin/python3
    - no_chown: True
    - require:
      - pip: virtualenv
      - file: {{ pillar['website']['venv_dir'] }}

install:
  cmd.run:
    - name: 'source /var/www/venv/bin/activate && pip install -r /var/www/requirements.txt'
    - cwd: /var/www
    - shell: /bin/bash
    - require:
      - virtualenv: {{ pillar['website']['venv_dir'] }}

migrate:
  cmd.run:
    - name: 'source /var/www/venv/bin/activate && python /var/www/manage.py migrate --noinput'
    - cwd: /var/www
    - shell: /bin/bash
    - require:
      - virtualenv: {{ pillar['website']['venv_dir'] }}

collectstatic:
  cmd.run:
    - name: 'source /var/www/venv/bin/activate && python /var/www/manage.py collectstatic --noinput'
    - cwd: /var/www
    - shell: /bin/bash
    - require:
      - virtualenv: {{ pillar['website']['venv_dir'] }}

messages:
  cmd.run:
    - name: |
        source /var/www/venv/bin/activate && python /var/www/manage.py makemessages --all --pythonpath=apps/ --ignore=venv/* -l en -l ru
        source /var/www/venv/bin/activate && python /var/www/manage.py compilemessages --pythonpath=apps/ -l en -l ru
    - cwd: /var/www
    - shell: /bin/bash
    - require:
      - virtualenv: {{ pillar['website']['venv_dir'] }}