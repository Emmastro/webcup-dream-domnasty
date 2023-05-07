import logging

from .models import Category, Dream, Post, Contact
from rest_framework import serializers
from django.contrib.auth.models import User


class DreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = ('id', 'dream', 'dream_date', 'sleep_time',
                  'wake_time', 'created_at', 'assessment')
        read_only_fields = ('id', 'created_at', 'assessment')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True, view_name='post-detail', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'owner']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['owner', 'id', 'title', 'content', 'author', 'category']


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = ['url', 'owner', 'id', 'name', 'email', 'message']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at')