copy-locale:
  file.managed:
    - name: /etc/default/locale
    - source: salt://locale/locale
    - template: jinja