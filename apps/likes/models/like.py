from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import (
    CASCADE, CharField, ForeignKey, Model, PositiveIntegerField)

from apps.user.models.user import User


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
    user = ForeignKey(User, related_name='likes', on_delete=CASCADE)
    like_type = CharField(max_length=2, choices=LIKED_CHOICES)
    content_type = ForeignKey(ContentType, on_delete=CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey()
