import pytest

from utils.factories import (
    AlbumFactory, ArtistFactory, GenreFactory, SongFactory)


@pytest.fixture
def album():
    return AlbumFactory.create(
        artists=ArtistFactory.create_batch(size=2),
        genres=GenreFactory.create_batch(size=2),
        songs=SongFactory.create_batch(size=6),
    )


@pytest.fixture
def genres():
    return GenreFactory.create_batch(size=2)


@pytest.fixture
def songs():
    return SongFactory.create_batch(size=4)


@pytest.fixture
def artists():
    return ArtistFactory.create_batch(size=3)


@pytest.fixture
def album_qty():
    return 1


@pytest.fixture
def albums(album_qty):
    return AlbumFactory.create_batch(size=album_qty)
