from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.likes import mixin_tools as likes_services
from apps.media.models.song import Song
from apps.media.serializers.artist import ArtistShortInfoSerializer
from apps.media.serializers.genre import GenreDetailSerializer


class SongDetailSerializer(ModelSerializer):
    genres = GenreDetailSerializer(many=True,)
    artists = ArtistShortInfoSerializer(many=True,)
    is_fan = SerializerMethodField()

    class Meta:
        model = Song
        fields = ('url', 'title', 'duration', 'image', 'file',
                  'listens', 'explicit', 'artists', 'genres',
                  'total_likes', 'is_fan')
        read_only_fields = ('listens', 'duration')

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


class SongShortInfoSerializer(SongDetailSerializer):
    class Meta(SongDetailSerializer.Meta):
        fields = ('url', 'title', 'duration', 'explicit', 'image')


class SongCUSerializer(ModelSerializer):
    class Meta(SongDetailSerializer.Meta):
        fields = ('url', 'title', 'image', 'file',
                  'explicit', 'artists', 'genres')

    def get_fields(self, *args, **kwargs):
        fields = super(SongCUSerializer, self).get_fields()
        request = self.context.get('request')
        if request and getattr(request, 'method', None) == "PUT":
            for field in fields.values():
                field.required = False
        return fields

    def create(self, validated_data):
        genres_data = validated_data.pop('genres')
        artists_data = validated_data.pop('artists')
        song = Song.objects.create(**validated_data)
        song.genres.add(*genres_data)
        song.artists.add(*artists_data)
        return song

    def update(self, instance, validated_data):
        genres_data = validated_data.pop('genres', None)
        artists_data = validated_data.pop('artists', None)
        instance = super(SongCUSerializer, self).update(instance,
                                                        validated_data)
        instance.save()
        if genres_data:
            instance.genres.set(genres_data)
        if artists_data:
            instance.artists.set(artists_data)
        return instance
