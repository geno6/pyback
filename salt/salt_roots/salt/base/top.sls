local:
  '*':
    - packages
    - python
    - postgresql
    - postgresql.postgis
    - redis
    - mongodb
    - nginx
    - cron
    - django.settings
    - django
    - django.superuser
    - circus

dev:
  '*':
    - git
    - packages
    - python
    - postgresql
    - postgresql.postgis
    - redis
    - mongodb
    - nginx
    - cron
    - django.settings
    - django
    - django.superuser
    - circus

prod:
  '*':
    - git
    - packages
    - python
    - postgresql
    - postgresql.postgis
    - redis
    - mongodb
    - nginx
    - cron
    - django.settings
    - django
    - django.superuser
    - circus