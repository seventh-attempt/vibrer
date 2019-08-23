from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User as BaseUser
from django.db.models import (Model, CharField, PositiveIntegerField, ImageField, FileField,
                              BooleanField, ManyToManyField, TextField, DateField,
                              PositiveSmallIntegerField, ForeignKey, CASCADE)


class Song(Model):
    title = CharField(max_length=200)
    duration = PositiveIntegerField()
    image = ImageField(upload_to='', default='')
    file = FileField(upload_to='', null=True)
    listens = PositiveIntegerField()
    explicit = BooleanField()
    hash = CharField(db_index=True)
    artists = ManyToManyField('Artist', related_name='songs')
    genres = ManyToManyField('Genre', related_name='songs')
    album = ManyToManyField('Album', related_name='songs')


class Artist(Model):
    stage_name = CharField(max_length=200)
    info = TextField(blank=True)
    photo = ImageField(upload_to='', default='')
    genre = ManyToManyField('Genre', related_name='artists')


class Album(Model):
    title = CharField(max_length=200)
    songs_amount = PositiveSmallIntegerField()
    photo = ImageField(upload_to='', default='')
    release_year = DateField()
    artist = ManyToManyField('Artist', related_name='albums')


class User(BaseUser):
    photo = ImageField(upload_to='', default='')
    playlists = ManyToManyField('Playlist', related_name='users')
    followers = ManyToManyField('User', related_name='followings')


class Playlist(Model):
    name = CharField(max_length=200, unique=True)
    is_private = BooleanField()
    songs = ManyToManyField('Song', related_name='playlists')


class Genre(Model):
    HH = 'Hip - Hop'
    REG = 'Reggae'
    POP = 'Pop'
    IND = 'Indie'
    ROCK = 'Rock'
    CLS = 'Classic'
    RdB = 'R & B'
    JAZZ = 'Jazz'
    GENRES = (
        (HH, 'Hip - Hop'),
        (REG, 'Reggae'),
        (POP, 'Pop'),
        (IND, 'Indie'),
        (ROCK, 'Rock'),
        (CLS, 'Classic'),
        (RdB, 'R & B'),
        (JAZZ, 'Jazz'),
    )
    name = CharField(choices=GENRES)


class Liked(Model):
    ARTIST = 'AR'
    SONG = 'SG'
    PLAYLIST = 'PT'
    ALBUM = 'AM'
    LIKED_CHOICES = (
        (ARTIST, 'Artist'),
        (SONG, 'Song'),
        (PLAYLIST, 'Playlist'),
        (ALBUM, 'Album'),
    )
    content_type = CharField(choices=LIKED_CHOICES)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey(content_type, object_id)
    user = ForeignKey(User, related_name='relations', on_delete=CASCADE)
