settings:
  file:
    - managed
    - name: {{ pillar['django']['settings_path'] }}
    - source: salt://django/settings.py
    - template: jinja