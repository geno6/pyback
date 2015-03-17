settings:
  file:
    - managed
    - name: {{ pillar['website']['settings_path'] }}
    - source: salt://website/settings.py
    - template: jinja