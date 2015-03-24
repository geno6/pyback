{% for k, v in pillar.get("cron", {}).items() %}
cron_job_{{ k }}:
  cron:
    - {{ v.ensure|default('present') }}
    - name: {{ v.cmd }}
    - identifier: {{ k }}
    - minute: '{{ v.minute|default('*') }}'
    - hour: '{{ v.hour|default('*') }}'
    - daymonth: '{{ v.daymonth|default('*') }}'
    - month: '{{ v.month|default('*') }}'
    - dayweek: '{{ v.dayweek|default('*') }}'
{% endfor %}