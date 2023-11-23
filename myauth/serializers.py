"""
from rest_framework import serializers
from myauth.models import APIKey

class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('api_key', 'secret_key', ) #'user')
        model = APIKey

class APIUserKeySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('api_key', 'secret_key', 'user')
        model = APIKey

"""