import json

import faker
import pytest


@pytest.mark.django_db
class TestLikes:
    def test_like_song(self, client, song, user, token):
        """
        test like song
        """
        res = client.post(
            f'/api/song/{song.id}/like/',
            content_type="application/json",
            **{'HTTP_AUTHORIZATION': 'Token ' + str(token)}
        )
        assert res.status_code == 200
        res = client.get(
            f'/api/song/{song.id}/fans/',
            content_type="application/json"
        )
        fans_dict = res.json()[0]
        assert user.id == fans_dict['id']
        assert user.username == fans_dict['username']

    def test_like_artist(self, client, artist, user, token):
        """
        test like artist
        """
        res = client.post(
            f'/api/artist/{artist.id}/like/',
            content_type="application/json",
            **{'HTTP_AUTHORIZATION': 'Token ' + str(token)}
        )
        assert res.status_code == 200
        res = client.get(
            f'/api/artist/{artist.id}/fans/',
            content_type="application/json"
        )
        fans_dict = res.json()[0]
        assert user.id == fans_dict['id']
        assert user.username == fans_dict['username']

    def test_like_album(self, client, album, user, token):
        """
        test like album
        """
        res = client.post(
            f'/api/album/{album.id}/like/',
            content_type="application/json",
            **{'HTTP_AUTHORIZATION': 'Token ' + str(token)}
        )
        assert res.status_code == 200
        res = client.get(
            f'/api/album/{album.id}/fans/',
            content_type="application/json"
        )
        fans_dict = res.json()[0]
        assert user.id == fans_dict['id']
        assert user.username == fans_dict['username']

    def test_remove_like(self, client, liked_song, user, song, token):
        """
        test remove like from song
        """
        res = client.get(
            f'/api/song/{song.id}/fans/',
            content_type="application/json"
        )
        fans_dict = res.json()[0]
        assert user.id == fans_dict['id']
        assert user.username == fans_dict['username']
        res = client.delete(
            f'/api/song/{song.id}/like/',
            content_type="application/json",
            **{'HTTP_AUTHORIZATION': 'Token ' + str(token)}
        )
        assert res.status_code == 200
        res = client.get(
            f'/api/song/{song.id}/fans/',
            content_type="application/json"
        )
        fans_dict = res.json()
        assert len(fans_dict) == 0

    def test_like_auth_error(self, client, song):
        """
        test like song without auth
        """
        res = client.post(
            f'/api/song/{song.id}/like/',
            content_type="application/json",
        )
        assert res.status_code == 401
        response = res.json()['detail']
        assert response == 'Authentication credentials were not provided.'

    def test_multiple_like(self, client, song, user, token):
        """
        test multiple like return 409 HTTP status
        """
        res = client.post(
            f'/api/song/{song.id}/like/',
            content_type="application/json",
            **{'HTTP_AUTHORIZATION': 'Token ' + str(token)}
        )
        assert res.status_code == 200
        res = client.post(
            f'/api/song/{song.id}/like/',
            content_type="application/json",
            **{'HTTP_AUTHORIZATION': 'Token ' + str(token)}
        )
        assert res.status_code == 409

    def test_dislike_error(self, client, song, user, token):
        """
        test remove not given like return 409 HTTP status
        """
        res = client.delete(
            f'/api/song/{song.id}/like/',
            content_type="application/json",
            **{'HTTP_AUTHORIZATION': 'Token ' + str(token)}
        )
        assert res.status_code == 409
