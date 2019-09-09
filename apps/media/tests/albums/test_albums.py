import pytest
import faker


@pytest.mark.django_db
class TestAlbums:
    def test_detail(self, client, album):
        """
        test albums details
            * check basic structure
        """
        res = client.get(f'/api/album/{album.id}')
        album_dict = res.json()
        fields = ('title', 'songs_amount', 'photo', 'release_year',
                  'artists', 'genres', 'songs', )
        assert res.status_code == 200
        assert all(album_dict.get(k) for k in fields)

    @pytest.mark.parametrize('album_qty', [0, 3, 5, 7, 10])
    def test_list(self, client, albums, album_qty):
        """
        test list of albums on getting right:
            * amount
            * data type
        """
        result = client.get('/api/album')

        assert result.status_code == 200
        assert isinstance(result.json(), list)
        assert len(result.json()) == album_qty

    def test_detail_error(self, client):
        """
        test album details for non-existing album
        """
        result = client.get(f'api/album/{faker.Faker().random_number(digits=30)}')

        assert result.status_code == 404
