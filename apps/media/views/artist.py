from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.media.models.artist import Artist
from apps.media.serializers.artist import ArtistSerializer


class ArtistListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genres']
