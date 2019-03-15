from rest_framework import status
from rest_framework.test import APITestCase


class TestIntegrationViews(APITestCase):
    """Recipe rest endpoints"""

    def test_seed_user(self):
        """it should return a list of recipes in the database"""
        response = self.client.post('/integration/', format='json')
        assert response.status_code == status.HTTP_201_CREATED

