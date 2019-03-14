from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

TEST_USER = {
    'username': 'testuser',
    'email': 'leesutton1@gmail.com',
    'password': 'password123!'
}


class SeedView(APIView):
    """
    View to seed and delete tests users
    """

    def post(self, request, format=None):
        """Seeds in an admin user"""
        # if is dev mode
        # seed in an admin user
        # User.objects.create_user(**TEST_USER)
        return Response(status=status.HTTP_201_CREATED)
