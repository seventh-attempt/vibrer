# from django.core.validators import validate_image_file_extension
from django.db.models import (
    BooleanField, CharField, ManyToManyField, Model,
    PositiveIntegerField, URLField)


class Song(Model):
    title = CharField(max_length=200)
    duration = PositiveIntegerField(default=0)
    image = URLField(default='image.png')
    file = URLField()
    listens = PositiveIntegerField(default=0)
    explicit = BooleanField(default=False)
    artists = ManyToManyField('Artist', related_name='songs')
    genres = ManyToManyField('Genre', related_name='songs')

    def __str__(self):
        return self.title
