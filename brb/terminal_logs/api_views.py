from rest_framework import generics
from rest_framework import permissions
from brb.terminal_logs.serializers import LogSerializer
from brb.terminal_logs.models import Log
from brb.terminal_logs.permissions import IsOwner


class LogsApi(generics.ListCreateAPIView):
    """
    Logs model API view
    * Requires token authentication
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner,)
    serializer_class = LogSerializer
    queryset = Log.objects.all()
