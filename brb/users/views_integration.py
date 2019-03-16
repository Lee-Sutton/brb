from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

TEST_USER = {
    'username': 'testuser',
    'email': 'leesutton1@gmail.com',
    'password': 'password123!'
}


class IntegrationView(APIView):
    """
    View to seed and delete tests users
    """

    def post(self, request, format=None):
        """Seeds in an admin user in dev mode only"""
        if settings.DEBUG:
            User.objects.create_superuser(**TEST_USER)
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_404_NOT_FOUND)


