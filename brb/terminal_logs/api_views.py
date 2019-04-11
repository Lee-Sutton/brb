from rest_framework.views import APIView
from rest_framework import authentication, status
from rest_framework.response import Response
from brb.terminal_logs.models import Log


class LogsApi(APIView):
    """
    Logs model API view
    * Requires token authentication
    """
    authentication_classes = (authentication.TokenAuthentication,)

    def post(self, request):
        log = Log(content=request.data['content'], user_id=request.user.id)
        log.save()
        return Response(status=status.HTTP_201_CREATED)
