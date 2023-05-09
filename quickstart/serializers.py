from django.contrib.auth.models import User, Group
from rest_framework import serializers

from quickstart.models import FriendRequest


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['from_id', 'to_id']


class OutcomingRequestSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='to_id.username')

    class Meta:
        model = FriendRequest
        fields = ['to_id', 'name']


class IncomingRequestSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='from_id.username')

    class Meta:
        model = FriendRequest
        fields = ['from_id', 'name']


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['from_id', 'to_id']

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
