from django.urls import reverse
#from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class MovieListTests(APITestCase):
    def test_get_movie_list_by_city(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('show_apis:movie_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CinemaListTests(APITestCase):
    def test_get_movie_list_by_city(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('show_apis:cinema_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
