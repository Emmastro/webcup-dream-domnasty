import logging

from .models import Dream
from rest_framework import serializers


class DreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = ('id', 'dream', 'dream_date', 'sleep_time', 'wake_time', 'created_at')
