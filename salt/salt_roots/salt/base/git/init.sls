{{ pillar["git"]["repo_url"] }}:
  git.latest:
    - rev: {{ pillar["git"]["branch"] }}
    - target: {{ pillar["django"]["src_dir"] }}
    - https_user: {{ pillar["git"]["username"] }}
    - https_pass: {{ pillar["git"]["password"] }}