from apps.user.models.user import User
from rest_framework import serializers
from apps.likes.models.like import Liked


class FanSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Liked
        fields = ('object_id', 'content_type', 'like_type')
