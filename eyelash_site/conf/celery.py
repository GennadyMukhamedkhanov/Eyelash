import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'conf.settings')

app = Celery('conf')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

# заносим таски в очередь
app.conf.beat_schedule = {
    'backup_db': {
        'task': 'my_site.tasks.backup_db',
        'schedule': 3.0,
       },
}