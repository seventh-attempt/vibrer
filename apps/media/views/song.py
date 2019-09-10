from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.media.models.song import Song
from apps.media.serializers.song import (
    SongDetailSerializer, SongShortInfoSerializer)


class SongListView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('genres', 'artists')

    def get_serializer_class(self):
        if hasattr(self, 'action') and self.action == 'retrieve':
            return SongDetailSerializer
        return SongShortInfoSerializer
