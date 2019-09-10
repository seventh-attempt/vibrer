from rest_framework import viewsets

from apps.media.models.genre import Genre
from apps.media.serializers.genre import GenreDetailSerializer


class GenreListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = GenreDetailSerializer
    queryset = Genre.objects.all()
