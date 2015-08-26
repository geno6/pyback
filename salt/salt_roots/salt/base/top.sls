local:
  '*':
    - apt
    - locale.configure
    - packages
    - python
    - postgresql
    - postgresql.postgis
    - redis
    - nginx
    - cron
    - django.settings
    - django
    - django.superuser
    - circus

dev:
  '*':
    - apt
    - git
    - locale.configure
    - packages
    - python
    - postgresql
    - postgresql.postgis
    - redis
    - nginx
    - cron
    - django.settings
    - django
    - django.superuser
    - circus

prod:
  '*':
    - apt
    - git
    - ssl
    - locale.configure
    - bower
    - python
    - postgresql
    - postgresql.postgis
    - redis
    - nginx
    - cron
    - django.settings
    - django
    - django.superuser
    - circus