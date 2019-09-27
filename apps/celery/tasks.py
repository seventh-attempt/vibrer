import datetime
from itertools import groupby

from django.core.cache import cache, caches
from django.core.exceptions import ObjectDoesNotExist

from apps.celery.celery import app
from apps.celery.models import Event
from apps.media.models import Song
from apps.user.models import User
from django_redis import get_redis_connection


# TODO fix
@app.task(name='aggregate_listen_info')
def aggregate_listen_info():
    con = get_redis_connection('default')
    print(con)
    keys = con.keys('*')
    print(keys)
    print([v.decode() for v in filter(bool, con.mget(*keys))])
    # print(con.(keys=keys))
    # grouped_values = [dict(v) for k, v in
    #                   groupby(cache.get_many(cache.keys("*")).items(), lambda x: x[0])]
    # for key, values in grouped_values:
    #     try:
    #         ids = key.split('-')[:-1]
    #         user = User.objects.get(pk=ids[0])
    #         song = Song.objects.get(pk=ids[1])
    #
    #         numbers = ([int(num) for num in v.decode().split('-')] for v in values)
    #         listen_duration = sum(abs(v[0] - v[1]) for v in numbers)
    #         # ^^^^^ top 2 strings can be replaced on vvvvv
    #         # listen_duration = sum((abs(eval(v.decode())) for v in values))
    #
    #         pct = listen_duration / song.duration if song.duration else 0
    #         kwargs = {
    #             'user': user,
    #             'song': song,
    #             'listen_percentage': round(pct, 2),
    #             'datetime': datetime.datetime.now().strftime("%d,%H")
    #         }
    #         Event.objects.update_or_create(**kwargs)
    #     except ObjectDoesNotExist:
    #         print(f'Celery worker skipped object: {key}{values}')
    pass
