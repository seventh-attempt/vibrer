from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
    CASCADE, DateTimeField, FloatField, Model, OneToOneField)
from apps.media.models.song import Song
from apps.user.models import User


class Event(Model):
    song = OneToOneField(Song, on_delete=CASCADE)
    user = OneToOneField(User, on_delete=CASCADE)
    datetime = DateTimeField()
    listen_percentage = FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
