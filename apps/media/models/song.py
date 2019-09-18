from django.core.validators import validate_image_file_extension
from django.db.models import (
    BooleanField, CharField, FileField, ImageField, ManyToManyField, Model,
    PositiveIntegerField)

from utils.validators import validate_file_size, validate_audio_file_extension


class Song(Model):
    title = CharField(max_length=200)
    duration = PositiveIntegerField(default=0)
    image = ImageField(default=None, validators=[validate_image_file_extension,
                                                 validate_file_size])
    file = FileField(validators=[validate_audio_file_extension,
                                 validate_file_size])
    listens = PositiveIntegerField(default=0)
    explicit = BooleanField(default=False)
    artists = ManyToManyField('Artist', related_name='songs')
    genres = ManyToManyField('Genre', related_name='songs')

    def __str__(self):
        return self.title
