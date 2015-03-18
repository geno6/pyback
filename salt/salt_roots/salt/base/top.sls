local:
  '*':
    - requirements
    - python
    - postgresql
    - redis
    - mongodb
    - nginx
    - circus
    - website.settings
    - website.django

dev:
  '*':
    - requirements
    - python
    - postgresql
    - redis
    - mongodb
    - nginx
    - circus
    - website.settings
    - website.django

prod:
  '*':
    - requirements
    - python
    - postgresql
    - redis
    - mongodb
    - nginx
    - circus
    - website.settings
    - website.django