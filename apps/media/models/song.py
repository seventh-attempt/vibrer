from django.db.models import Model, CharField, PositiveIntegerField, BooleanField, ManyToManyField
from django.forms import ImageField, FileField
from .artist import Artist
from .album import Album
from .genre import Genre


class Song(Model):
    title = CharField(max_length=200)
    duration = PositiveIntegerField()
    image = ImageField(upload_to='', default='')
    file = FileField(upload_to='', null=True)
    listens = PositiveIntegerField()
    explicit = BooleanField()
    artists = ManyToManyField(Artist, related_name='songs')
    genres = ManyToManyField(Genre, related_name='songs')
    album = ManyToManyField(Album, related_name='songs')

