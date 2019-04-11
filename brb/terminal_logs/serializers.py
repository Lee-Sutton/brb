from rest_framework import serializers
from brb.terminal_logs.models import Log


class LogSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Log
        fields = ('id', 'content', 'user')
