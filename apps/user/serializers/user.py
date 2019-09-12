from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField

from apps.user.models.user import User
from apps.media.serializers.song import SongShortInfoSerializer
from apps.user.serializers.playlist import PlaylistShortInfoSerializer


class FollowerSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('url',)


class UserSerializer(ModelSerializer):
    followers = HyperlinkedRelatedField(many=True, read_only=True, view_name='user-detail')
    playlists = HyperlinkedRelatedField(many=True, read_only=True, view_name='playlist-detail')
    liked_songs = HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # followers = FollowerSerializer(many=True,)
    # playlists = PlaylistShortInfoSerializer(many=True,)
    # liked_songs = SongShortInfoSerializer(many=True,)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'photo', 'followers',
                  'followers_amount', 'playlists', 'liked_songs', 'is_staff')


class UserShortInfoSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        fields = ('url', 'username', 'photo', 'followers',
                  'followers_amount', 'playlists')
