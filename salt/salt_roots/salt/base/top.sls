local:
  '*':
    - requirements
    - python
    - postgresql
    - postgresql.postgis
    - redis
    - mongodb
    - nginx
    - cron
    - django
    - django.settings
    - django.superuser
    - circus

dev:
  '*':
    - git
    - requirements
    - python
    - postgresql
    - postgresql.postgis
    - redis
    - mongodb
    - nginx
    - cron
    - django
    - django.settings
    - django.superuser
    - circus

prod:
  '*':
    - git
    - requirements
    - python
    - postgresql
    - postgresql.postgis
    - redis
    - mongodb
    - nginx
    - cron
    - django
    - django.settings
    - django.superuser
    - circus