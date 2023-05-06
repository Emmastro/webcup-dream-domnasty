import logging
from django.conf import settings

from .models import Client
from rest_framework import serializers
# from dj_rest_auth.utils import import_callable
# from dj_rest_auth.serializers import UserDetailsSerializer as DefaultUserDetailsSerializer
from dj_rest_auth.models import TokenModel


rest_auth_serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})

# UserDetailsSerializer = import_callable(
#     rest_auth_serializers.get('USER_DETAILS_SERIALIZER', DefaultUserDetailsSerializer)
# )


class ClientSerializer(serializers.ModelSerializer):
    """
    Docs
    """
    class Meta:
        model = Client
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')


class CustomTokenSerializer(serializers.ModelSerializer):
    """
    Docs
    """

    user = ClientSerializer(read_only=True)

    class Meta:
        model = TokenModel
        fields = ('key', 'user', )



