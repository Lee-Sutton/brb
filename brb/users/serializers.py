from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.Models):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
