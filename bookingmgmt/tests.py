from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient   

class LoggedOutBookingTests(APITestCase):
    def test_booking(self):
        """
        Ensure we can create a new booking against a specific show
        """
        url = reverse('booking_apis:book_show')
        data = {"show_id": 1, "seat_count": 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


"""
class LoggedInBookingTests(APITestCase):
    def test_booking(self):
        # Include an appropriate `Authorization:` header on all requests.
        token = Token.objects.get(user__username='admin')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        url = reverse('booking_apis:book_show')
        data = {"show_id": 1, "seat_count": 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
"""
