from django.db.models import Model, CharField, TextField, ManyToManyField
from django.forms import ImageField
from .genre import Genre


class Artist(Model):
    stage_name = CharField(max_length=200)
    info = TextField(blank=True)
    photo = ImageField(upload_to='', default='')
    genre = ManyToManyField(Genre, related_name='artists')
