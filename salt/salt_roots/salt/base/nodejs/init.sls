nodejs:
  pkg:
    - installed
npm:
  pkg:
    - installed

/usr/bin/node:
  file.symlink:
    - target: /usr/bin/nodejs
    - require:
      - pkg: npm

bower:
  npm.installed:
    - require:
      - pkg: npm