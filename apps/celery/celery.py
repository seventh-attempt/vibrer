from __future__ import absolute_import

from datetime import timedelta

from celery import Celery
from django.conf import settings

from vibrer.settings import REDIS_URL

app = Celery('vibrer', broker=REDIS_URL)
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(packages=settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'aggregate_listen_info': {
        'task': 'aggregate_listen_info',
        'schedule': timedelta(seconds=30)  # crontab(minute='*/15')
    }
}
