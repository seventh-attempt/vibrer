from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from django_redis import get_redis_connection

from apps.media.models.song import Song
from apps.media.serializers.song import (
    SongCUSerializer, SongDetailSerializer, SongShortInfoSerializer)


class SongView(ModelViewSet):
    queryset = Song.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('genres', 'artists',)
    http_method_names = ('get', 'post', 'put')

    def get_serializer_class(self):
        method = getattr(self.request, 'method', None)
        action = getattr(self, 'action', None)
        if self.request and method == 'GET':
            if action == 'list':
                return SongShortInfoSerializer
            elif action == 'retrieve':
                return SongDetailSerializer
        elif self.request and method in ('POST', 'PUT'):
            return SongCUSerializer

    def get_permissions(self):
        return [IsAuthenticatedOrReadOnly(), ]

    @action(methods=['POST'], detail=True)
    def listen(self, request, *args, **kwargs):
        start_second = request.data.get('start_second')
        end_second = request.data.get('end_second')
        song = Song.objects.get(pk=kwargs['pk'])

        if not all([
            start_second is not None,
            end_second,
            start_second < end_second,
            start_second >= 0,
            (end_second - start_second) <= 30,
            end_second <= song.duration,
        ]):
            return Response({'Details': 'You have to set correct '
                                        '\'start_second\' and \'end_second\' '
                                        'parameters'}, status=HTTP_400_BAD_REQUEST)

        user = request.user
        con = get_redis_connection('default')
        con.sadd(f'{user}-{song}-piece', f'{start_second}-{end_second}')

        return Response({'title': song.title, 'duration': song.duration, 'cached-pieces': con.smembers(f'{user}-{song}-piece')})
