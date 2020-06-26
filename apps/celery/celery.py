from celery import Celery
from celery.schedules import crontab
from django.conf import settings

from vibrer.settings import REDIS_URL, RABBIT_URL


# need different db for workers to avoid interferences
app1 = Celery('vibrer', broker=f'{REDIS_URL[:-1]}0')
app1.config_from_object('django.conf:settings')

app1.autodiscover_tasks(packages=settings.INSTALLED_APPS)

app1.conf.beat_schedule = {
    'aggregate_listen_info': {
        'task': 'aggregate_listen_info',
        'schedule': 30.0
    }
}

app2 = Celery('vibrer', backend='rpc://', broker=f'{RABBIT_URL}')
app2.config_from_object('django.conf:settings')

app2.autodiscover_tasks(packages=settings.INSTALLED_APPS)
