from allauth.account.models import EmailAddress
from django.contrib.auth import authenticate
from rest_auth.serializers import LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (CharField, EmailField,
                                        ModelSerializer, HyperlinkedRelatedField)
from apps.user.models.user import User


class UserRegistrationSerializer(ModelSerializer):
    # email = EmailField(required=True)
    # username = CharField(min_length=5, max_length=20, required=True)
    # password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        EmailAddress.objects.create(user=user, email=user.email)
        return user

    def save(self, request):
        data = request.data

        # if self.instance:
        #     self.instance = self.update(instance=self.instance, **data)
        # else:
        user_serializer = UserSerializer(data=data)
        user_serializer.is_valid()
        self.instance = self.create(user_serializer.validated_data)

        return self.instance


class UserLoginSerializer(ModelSerializer):
    # username = CharField(min_length=5, max_length=20, required=True)
    # password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password')
        read_only_fields = ('email',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


    # def _validate_password(self, username, password):
    #
    #     if username and password:
    #         user = authenticate(username=username, password=password)
    #     else:
    #         raise ValidationError('Check the data you\'ve entered')
    #
    #     return user
    #
    # def validate(self, attrs):
    #     username = attrs.get('username')
    #     password = attrs.get('password')
    #     user = self._validate_password(username, password)
    #     attrs['user'] = user
    #     return attrs


class UserSerializer(ModelSerializer):
    followers = HyperlinkedRelatedField(many=True, read_only=True, view_name='user-detail')
    playlists = HyperlinkedRelatedField(many=True, read_only=True, view_name='playlist-detail')
    liked_songs = HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # followers = FollowerSerializer(many=True,)
    # playlists = PlaylistShortInfoSerializer(many=True,)
    # liked_songs = SongShortInfoSerializer(many=True,)

    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email', 'photo', 'followers',
                  'followers_amount', 'playlists', 'liked_songs', 'is_staff')


class UserShortInfoSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        fields = ('url', 'username', 'photo', 'followers',
                  'followers_amount', 'playlists')
