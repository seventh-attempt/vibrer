from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate

from apps.user.models.user import User
from apps.user.serializers.user import (
    UserSerializer, UserShortInfoSerializer, UserRegistrationSerializer,
    UserLoginSerializer
)


class UserView(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ('get',)

    def get_serializer_class(self):
        if getattr(self, 'action', None) == 'list':
            return UserShortInfoSerializer

        return UserSerializer


class UserRegistrationView(ViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    # @action(detail=True, mehtods=['post'])
    def post(self, request):

        return Response(status=HTTP_201_CREATED)


class UserLoginView(APIView):
    # permission_classes = ()
    serializer_class = UserLoginSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Wrong Credentials'}, status=HTTP_400_BAD_REQUEST)
