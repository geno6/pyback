supervisor:
    pkg:
        - installed
    service.running:
        - watch:
            - file: /etc/supervisor/conf.d/*
        - require:
            - pkg: supervisor

celery_app:
    file.managed:
        - name: /etc/supervisor/conf.d/celery.conf
        - source: salt://supervisord/celery.conf
        - template: jinja
        - user: root
        - group: root
        - mode: 644
        - require:
            - pkg: supervisor