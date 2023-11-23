from celery import shared_task
import subprocess
import datetime
import os
from django.conf import settings

@shared_task
def backup_db():
    db_name = 'postgres'
    db_user = 'postgres'
    db_host = 'db'  # replace with your PostgreSQL service name
    backup_file = os.path.join(settings.BASE_DIR, 'db_backups', f'{db_name}_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.sql')
    command = f'pg_dump -h {db_host} -U {db_user} {db_name} > {backup_file}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print('Backup succeeded')
    else:
        print('Backup failed')
        print(result.stderr)

@shared_task
def write_to_log():
    log_file = os.path.join(settings.BASE_DIR, 'log.txt')
    with open(log_file, 'a') as f:
        f.write(f'Log entry at {datetime.datetime.now()}\n')