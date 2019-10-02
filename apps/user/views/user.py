from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import logout as django_logout
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.openapi import Response as SwaggerResponse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.user.serializers.user import (
    UserLoginSerializer, UserRegistrationSerializer, UserSerializer,
    UserShortInfoSerializer)

User = get_user_model()


# @method_decorator(name='', decorator=swagger_auto_schema(
#     operation_description='# ',
#     responses={
#         '200': SwaggerResponse(
#             '',
#             UserSerializer()
#         ),
#         '400': 'Bad request',
#         '401': 'Unauthorized',
#         '403': 'Permission denied'
#     }
# ))
class UserView(ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ('get',)

    def get_serializer_class(self):
        if getattr(self, 'action', None) == 'list':
            return UserShortInfoSerializer

        return UserSerializer


# @method_decorator(name='', decorator=swagger_auto_schema(
#     operation_description='# ',
#     responses={
#         '200': SwaggerResponse(
#             '',
#             UserSerializer()
#         ),
#         '401': 'Unauthorized',
#         '404': "Modelname with specified id doesn't exist"
#     }
# ))
class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        email = request.data.get('email', {})
        username = request.data.get('username', {})
        password = request.data.get('password', {})
        user = {'email': email, 'username': username, 'password': password}

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=HTTP_201_CREATED)


# @method_decorator(name='', decorator=swagger_auto_schema(
#     operation_description='# ',
#     responses={
#         '200': SwaggerResponse(
#             '',
#             UserLoginSerializer()
#         )
#     }
# ))
class UserLoginView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({'id': user.id, 'token': token.key},
                        status=HTTP_200_OK)


class UserLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        if getattr(settings, 'REST_SESSION_LOGIN', True):
            django_logout(request)

        response = Response({'details': 'Logged out successfully'},
                            status=HTTP_200_OK)

        return response


# @method_decorator(name='', decorator=swagger_auto_schema(
#     operation_description='# ',
#     responses={
#         '200': SwaggerResponse(
#             '',
#             UserSerializer()
#         ),
#         '400': 'Bad request',
#         '401': 'Unauthorized',
#         '403': 'Permission denied',
#         '404': "Modelname with specified id doesn't exist"
#     }
# ))
class UserGetDetailsView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
