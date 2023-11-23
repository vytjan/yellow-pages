# django_celery/celery.py

import os
from celery import Celery
from celery.schedules import crontab
from django_project.tasks import backup_db, write_to_log

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
app = Celery("django_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_connection_retry_on_startup = True

app.conf.beat_schedule = {
    'write-to-log-every-minute': {
        'task': 'django_project.tasks.write_to_log',
        'schedule': crontab(minute='*/5'),
    },
        'backup-every-1-minutes': {
        'task': 'django_project.tasks.backup_db',
        'schedule': crontab(minute='*/5'),
    },
}

app.autodiscover_tasks()