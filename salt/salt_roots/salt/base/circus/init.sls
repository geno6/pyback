circus:
  pip.installed:
    - name: circus

circus_upstart:
  file.managed:
    - name: /etc/init/circusd.conf
    - source: salt://circus/circusd.conf
    - template: jinja

circus_conf:
  file.managed:
    - name: /etc/circus.ini
    - source: salt://circus/circus.ini
    - template: jinja

circus_dir:
  file.directory:
    - name: /etc/circus.d

circusd:
  service:
    - running
    - user: root
    - group: root
    - require:
      - file: circus_upstart
      - file: circus_dir