import logging

from .models import Dream, Post
from rest_framework import serializers
from django.contrib.auth.models import User


class DreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = ('id', 'dream', 'dream_date', 'sleep_time', 'wake_time', 'created_at', 'assessment')
        # view only fields
        read_only_fields = ('id', 'created_at', 'assessment')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail',read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'owner']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Post
        fields = ['url', 'owner', 'id', 'title', 'content', 'author']

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance