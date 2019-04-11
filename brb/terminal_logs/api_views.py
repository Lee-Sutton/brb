from rest_framework.views import APIView
from rest_framework import authentication, status
from rest_framework.response import Response
from brb.terminal_logs.serializers import LogSerializer


class LogsApi(APIView):
    """
    Logs model API view
    * Requires token authentication
    """
    authentication_classes = (authentication.TokenAuthentication,)

    def post(self, request):
        log = LogSerializer(data=request.data, context={'request': request})
        if log.is_valid():
            log.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
