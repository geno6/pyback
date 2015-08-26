createsuperuser:
  cmd.run:
    - name: 'source {{ pillar['venv']['dir'] }}/bin/activate && ./manage.py superuser'
    - cwd: {{ pillar['django']['src_dir'] }}
    - shell: /bin/bash
    - require:
      - virtualenv: {{ pillar['venv']['dir'] }}