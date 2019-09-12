from rest_framework import viewsets

from apps.user.models.user import User
from apps.user.serializers.user import (
    UserSerializer, UserShortInfoSerializer)


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ('get',)

    def get_serializer_class(self):
        if getattr(self, 'action', None) == 'list':
            return UserShortInfoSerializer

        return UserSerializer
