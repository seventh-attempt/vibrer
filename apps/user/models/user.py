from django.db.models import (BooleanField, CharField, EmailField, ImageField,
                              IntegerField, ManyToManyField, Model)

from apps.media.models.song import Song
from apps.user.models.playlist import Playlist


class User(Model):
    username = CharField(max_length=50)
    email = EmailField(max_length=50)
    password = CharField(max_length=50)
    photo = ImageField(default=None, upload_to='media/')
    followers = ManyToManyField('User', blank=True, related_name='users')
    followers_amount = IntegerField(default=0)
    playlists = ManyToManyField(Playlist, blank=True, related_name='users')
    liked_songs = ManyToManyField(Song, blank=True, related_name='users')
    is_staff = BooleanField()
