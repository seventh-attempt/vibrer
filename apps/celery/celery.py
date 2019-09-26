from __future__ import absolute_import
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from datetime import timedelta

from vibrer.settings import REDIS_URL

app = Celery('vibrer', broker=REDIS_URL)
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(packages=settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'aggregate_listen_info': {
        'task': 'apps.celery.tasks.aggregate_listen_info',
        'schedule': crontab(minute='*/15')  # timedelta(seconds=30)
    }
}