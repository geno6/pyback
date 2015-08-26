createsuperuser:
  file:
    - managed
    - name: {{ pillar["django"]["src_dir"] }}/apps/core/cli/management/commands/superuser.py
    - source: salt://django/superuser.py
    - template: jinja