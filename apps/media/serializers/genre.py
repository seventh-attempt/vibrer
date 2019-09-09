from rest_framework import serializers
from apps.media.models.genre import Genre


class GenreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('url', 'pk', 'name', )


class GenreShortInfoSerializer(GenreDetailSerializer):
    # will be replaced by GenreDetailSerializer when we will remove 'pk' field from it.
    class Meta(GenreDetailSerializer.Meta):
        fields = ('url', 'name', )
