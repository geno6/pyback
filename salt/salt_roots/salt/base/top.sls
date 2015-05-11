local:
  '*':
    - apt
    - locale.configure
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
    - apt
    - locale
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
    - apt
    - locale
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