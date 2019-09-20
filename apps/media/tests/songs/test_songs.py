import json
import os

import faker
import pytest
from mutagen.mp3 import MP3


@pytest.mark.django_db
class TestSongs:
    def test_detail(self, client, song):
        """
        test song details
            * check basic structure
        """
        res = client.get(f'/api/song/{song.id}/')
        song_dict = res.json()
        assert res.status_code == 200
        assert isinstance(song_dict.get('title'), str)
        assert isinstance(song_dict.get('duration'), int)
        assert isinstance(song_dict.get('image'), str)
        assert isinstance(song_dict.get('file'), str)
        assert isinstance(song_dict.get('listens'), int)
        assert isinstance(song_dict.get('artists'), list)
        assert isinstance(song_dict.get('genres'), list)
        assert song_dict.get('explicit') in (True, False)

    @pytest.mark.parametrize('song_qty', [0, 5, 10, 25, 45])
    def test_list(self, client, songs, song_qty):
        """
        test list of songs on getting right:
            * amount
            * data type
        """
        res = client.get('/api/song/')
        assert res.status_code == 200
        assert isinstance(res.json(), list)
        assert len(res.json()) == song_qty

    def test_detail_error(self, client):
        """
        test song details for non-existing song
        """
        res = client.get(
            f'/api/song/{faker.Faker().random_number(digits=30)}/')
        assert res.status_code == 404

    def test_create(self, client, artists, genres):
        """
        test song create endpoint
        """
        title = faker.Faker().pystr(min_chars=5, max_chars=15)
        explicit = faker.Faker().pybool()
        genres = [genre.id for genre in genres]
        artists = [artist.id for artist in artists]
        with open('test/song.mp3', 'rb') as file:
            duration = round(MP3(file).info.length)
            data = {
                'title': title,
                'duration': duration,
                'explicit': explicit,
                'file': file,
                'genres': genres,
                'artists': artists
            }
            res = client.post('/api/song/', data=data)
            song_dict = res.json()
            assert res.status_code == 201
            assert song_dict.get("title") == title
            assert song_dict.get("duration") == duration
            assert song_dict.get("explicit") == explicit
            assert song_dict.get("genres") == genres
            assert song_dict.get("artists") == artists
            file_name = song_dict.get('file').rsplit('/', 1)[-1]
            os.remove(f'media/{file_name}')

    def test_update_m2m(self, client, song, genres):
        """
        test song update m2m field genres
        """
        title = faker.Faker().pystr(min_chars=5, max_chars=15)
        genres = [genre.id for genre in genres]
        data = {"genres": genres, "title": title}
        data = json.dumps(data)
        res = client.put(f'/api/song/{song.id}/', data=data,
                         content_type="application/json")
        song_dict = res.json()
        assert res.status_code == 200
        assert song_dict.get("title") == title
        assert song_dict.get("genres") == genres
