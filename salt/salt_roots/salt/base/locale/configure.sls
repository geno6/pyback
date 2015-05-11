include:
  - locale

configure-locale:
  cmd.run:
    - name: locale-gen en_US.UTF-8 & sudo dpkg-reconfigure locales
    - watch:
      - file: /etc/default/locale