from django.db.models import Model, CharField, PositiveSmallIntegerField, DateField, ManyToManyField
from django.forms import ImageField
from .artist import Artist


class Album(Model):
    title = CharField(max_length=200)
    songs_amount = PositiveSmallIntegerField()
    photo = ImageField(upload_to='', default='')
    release_year = DateField()
    artist = ManyToManyField(Artist, related_name='albums')
