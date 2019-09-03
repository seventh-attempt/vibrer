from rest_framework import viewsets
from apps.media.models.album import Album
from apps.media.serializers.album import AlbumSerializer, AlbumDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response


class AlbumListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['genres', 'artists']
    ordering_fields = ['release_year']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AlbumDetailSerializer(instance)
        return Response(serializer.data)
