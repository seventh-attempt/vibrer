from rest_framework import serializers
from apps.media.models.artist import Artist


class ArtistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class ArtistForAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('stage_name', 'photo',)
