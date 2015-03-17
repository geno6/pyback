python:
  pkg:
    - installed
    - names:
      - python-dev
      - python3-dev
      - python

pip:
  pkg:
    - installed
    - name: python-pip
    - require:
      - pkg: python

virtualenv:
  pip:
    - installed
    - require:
      - pkg: pip
