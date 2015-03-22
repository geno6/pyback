include:
  - postgresql

postgis-packages:
  pkg.installed:
    - names:
      - postgis
      - postgresql-9.3-postgis-2.1
      - libgdal-dev
    - require:
      - pkg: postgresql

postgis-template:
  file.managed:
    - name: /etc/postgresql/9.3/main/postgis.sh
    - source: salt://postgresql/postgis.sh
    - template: jinja
    - user: postgres
    - group: postgres
    - mode: 755
  cmd.run:
    - name: bash /etc/postgresql/9.3/main/postgis.sh
    - user: postgres
    - cwd: /var/lib/postgresql
    - unless: psql -U postgres -l|grep {{ pillar["postgresql"]["database"] }}
    - require:
      - pkg: postgis-packages
      - file: postgis-template
      - pkg: postgresql