cron:
  log_something:
    ensure: present
    cmd: 'echo "Cron job done"'
    minute: '*'
    hour: '*'
    daymonth: '*'
    month: '*'
    dayweek: '*'