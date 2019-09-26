import datetime
from itertools import groupby

from django.core.cache import caches
from django.core.exceptions import ObjectDoesNotExist

from apps.celery.celery import app
from apps.celery.models import Event
from apps.media.models import Song
from apps.user.models import User
from django_redis import get_redis_connection

# cacheImitation = {
#     "23-4-piece": [b"160-161", b"239-240", b"0-20", b"20-36"],
#     "23-3-piece": [b"12-25", b"74-99"],
#     "21-3-piece": [b"90-120", b"120-159"],
#     "25-4-piece": [b"215-220", b"0-4", b"5-24"],
#     "21-4-piece": [b"15-30", b"160-190", b"0-14", b"40-53", b"56-90"],
# }


@app.task
def aggregate_listen_info():
    con = get_redis_connection('default')
    print(con)
    print(caches, caches['default'].keys('*'))
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
