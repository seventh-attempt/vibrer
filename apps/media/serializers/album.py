from rest_framework.serializers import ModelSerializer
from apps.media.models.album import Album
from apps.media.serializers.artist import ArtistForAlbumSerializer


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ('songs_amount',)


class AlbumDetailSerializer(ModelSerializer):
    artists = ArtistForAlbumSerializer(many=True,)

    class Meta:
        model = Album
        fields = '__all__'
