from rest_framework import serializers

from apps.media.models.song import Song
from apps.media.serializers.artist import ArtistShortInfoSerializer
from apps.media.serializers.genre import GenreShortInfoSerializer


class SongDetailSerializer(serializers.ModelSerializer):
    genres = GenreShortInfoSerializer(many=True,)
    artists = ArtistShortInfoSerializer(many=True, )

    class Meta:
        model = Song
        fields = ('url', 'pk', 'title', 'duration', 'image', 'file',
                  'listens', 'explicit', 'artists', 'genres')
        read_only_fields = ('listens', 'duration')


class SongShortInfoSerializer(SongDetailSerializer):
    class Meta(SongDetailSerializer.Meta):
        fields = ('url', 'title', 'duration', 'image', )
