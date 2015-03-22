superuser:
  file:
    - managed
    - name: {{ pillar["django"]["src_dir"] }}/apps/core/management/commands/superuser.py
    - source: salt://django/superuser.py
    - template: jinja