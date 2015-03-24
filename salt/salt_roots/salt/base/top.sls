local:
  '*':
    - requirements
    - python
    - postgresql
    - postgresql.postgis
    - redis
    - mongodb
    - nginx
    - circus
    - cron
    - django
    - django.settings
    - django.superuser

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
    - circus
    - cron
    - django
    - django.settings
    - django.superuser

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
    - circus
    - cron
    - django
    - django.settings
    - django.superuser