from rest_framework import serializers
from apps.media.models.artist import Artist
from apps.media.serializers.genre import GenreShortInfoSerializer


class ArtistSerializer(serializers.ModelSerializer):
    genres = GenreShortInfoSerializer(many=True,)

    class Meta:
        model = Artist
        fields = ('url', 'pk', 'stage_name', 'info', 'photo', 'genres')


class ArtistShortInfoSerializer(ArtistSerializer):
    class Meta(ArtistSerializer.Meta):
        fields = ('url', 'stage_name', 'photo',)
