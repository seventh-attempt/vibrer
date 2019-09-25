import pytest


from utils.factories import LikedSongFactory


@pytest.fixture
def liked_song(user, song):
    return LikedSongFactory.create(
        user=user,
        content_object=song
    )
