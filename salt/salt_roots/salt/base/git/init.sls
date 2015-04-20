{{ pillar["git"]["repo_url"] }}:
  git.latest:
    - rev: {{ pillar["git"]["branch"] }}
    - target: {{ pillar["django"]["src_dir"] }}