{{ pillar['venv']['dir'] }}:
  file:
    - directory
    - makedirs: True

  virtualenv:
    - managed
    - distribute: True
    - python: /usr/bin/python3
    - no_chown: True
    - require:
      - pip: virtualenv
      - file: {{ pillar['venv']['dir'] }}

install:
  cmd.run:
    - name: 'source {{ pillar['venv']['dir'] }}/bin/activate && pip install -r requirements.txt'
    - cwd: {{ pillar['django']['src_dir'] }}
    - shell: /bin/bash
    - require:
      - virtualenv: {{ pillar['venv']['dir'] }}

migrate:
  cmd.run:
    - name: 'source {{ pillar['venv']['dir'] }}/bin/activate && ./manage.py migrate --noinput'
    - cwd: {{ pillar['django']['src_dir'] }}
    - shell: /bin/bash
    - require:
      - virtualenv: {{ pillar['venv']['dir'] }}

collectstatic:
  cmd.run:
    - name: 'source {{ pillar['venv']['dir'] }}/bin/activate && ./manage.py collectstatic --noinput'
    - cwd: {{ pillar['django']['src_dir'] }}
    - shell: /bin/bash
    - require:
      - virtualenv: {{ pillar['venv']['dir'] }}

superuser:
  file:
    - managed
    - name: {{ pillar["django"]["src_dir"] }}/apps/core/cli/management/commands/superuser.py
    - source: salt://django/superuser.py
    - template: jinja