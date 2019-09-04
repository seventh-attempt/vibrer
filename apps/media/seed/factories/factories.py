import factory
import faker
import django

from os import environ
from random import randint

environ.setdefault('DJANGO_SETTINGS_MODULE', 'vibrer.settings')
django.setup()

from apps.media.models.artist import Artist
from apps.media.models.album import Album
from apps.media.models.genre import Genre
from apps.media.models.song import Song


GENRES = [
    'Hip - Hop',
    'Reggae',
    'Pop',
    'Indie',
    'Rock',
    'Classic',
    'R & B',
    'Jazz',
]

faker = faker.Faker()


class GenreFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: GENRES[n])

    class Meta:
        model = Genre


class ArtistFactory(factory.django.DjangoModelFactory):
    stage_name = factory.LazyAttribute(lambda x: faker.name())
    info = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=200))

    class Meta:
        model = Artist

    @factory.post_generation
    def genre(self, create, extracted):
        if not create:
            return

        if extracted:
            for gn in [extracted]:
                self.genre.add(gn)


class SongFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.pystr(min_chars=5, max_chars=15))
    duration = factory.LazyAttribute(lambda x: faker.pyint(min_value=30, max_value=300))
    listens = factory.LazyAttribute(lambda x: faker.pyint())
    explicit = factory.LazyAttribute(lambda x: faker.pybool())

    class Meta:
        model = Song

    @factory.post_generation
    def artists(self, create, extracted):
        if not create:
            return

        if extracted:
            for gn in [extracted]:
                self.artists.add(gn)

    @factory.post_generation
    def genres(self, create, extracted):
        if not create:
            return

        if extracted:
            for gn in [extracted]:
                self.genres.add(gn)


class AlbumFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.pystr(min_chars=5, max_chars=15))
    songs_amount = 5
    release_year = factory.LazyAttribute(lambda x: faker.date_between(start_date='-30y', end_date='now'))

    class Meta:
        model = Album

    @factory.post_generation
    def artists(self, create, extracted):
        if not create:
            return

        if extracted:
            for ar in [extracted]:
                self.artists.add(ar)

    @factory.post_generation
    def genres(self, create, extracted):
        if not create:
            return

        if extracted:
            for gn in [extracted]:
                self.genres.add(gn)

    @factory.post_generation
    def songs(self, create, extracted):
        if not create:
            return

        if extracted:
            for so in [extracted]:
                self.songs.add(so)


def fill_with_data(data_type, lower_border, higher_border):
    return set(data_type[randint(0, len(data_type)-1)] for _ in range(randint(lower_border, higher_border)))


def fill(amount=50):
    Album.objects.all().delete()
    Artist.objects.all().delete()
    Genre.objects.all().delete()
    Song.objects.all().delete()

    # creating genres here
    for _ in range(len(GENRES)):
        GenreFactory.create()

    # creating artists here
    genres = Genre.objects.all()
    for _ in range(amount//3):
        # genres_set = fill_with_data(genre, 1, 3)
        ArtistFactory.create(genre=(genres[randint(0, genres.count()-1)]))

    # creating songs here
    artists = Artist.objects.all()
    for _ in range(amount):
        # artists_set = fill_with_data(genre, 1, 3)
        # genres_set = fill_with_data(genre, 1, 3)
        SongFactory.create(artists=(artists[randint(0, artists.count()-1)]),
                           genres=(genres[randint(0, genres.count()-1)]))

    # creating albums here
    songs = Song.objects.all()
    for _ in range(amount//4):
        # artists_set = fill_with_data(genre, 1, 3)
        # genres_set = fill_with_data(genre, 1, 3)
        # songs_set = fill_with_data(genre, 5, 10)
        AlbumFactory.create(artists=(artists[randint(0, artists.count()-1)]),
                            genres=(genres[randint(0, genres.count()-1)]),
                            songs=(songs[randint(0, songs.count()-1)]))
