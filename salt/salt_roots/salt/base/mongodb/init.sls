mongodb_server:
  pkg:
    - installed
    - pkgs:
      - mongodb
  service:
    - running
    - name: mongodb
    - enable: true

mongodb_user_{{ pillar["mongodb"]["user"] }}:
  mongodb_user.present:
    - name: {{ pillar["mongodb"]["user"] }}
    - passwd: {{ pillar["mongodb"]["password"] }}
    - database: {{ pillar["mongodb"]["database"] }}
    - require:
      - service: mongodb_server