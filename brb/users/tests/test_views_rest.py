from rest_framework import status
from rest_framework.test import APITestCase


class TestRecipeViews(APITestCase):
    """Recipe rest endpoints"""

    def test_recipe_list(self):
        """it should return a list of recipes in the database"""
        response = self.client.post('/api/v1/seed/user', format='json')
        assert response.status_code == status.HTTP_200_OK

