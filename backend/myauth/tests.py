from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_register_user(self):
        # Test successful user registration
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test duplicate registration (username already exists)
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user(self):
        # Create a user for login
        data = {'username': 'testuser', 'password': 'testpassword'}
        self.client.post(self.register_url, data)

        # Test successful login
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIn('user_id', response.data)
        self.assertIn('username', response.data)

        # Test invalid login credentials
        invalid_data = {'username': 'testuser', 'password': 'wrongpassword'}
        response = self.client.post(self.login_url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout_user(self):
        # Create a user for logout
        data = {'username': 'testuser', 'password': 'testpassword'}
        self.client.post(self.register_url, data)
        login_response = self.client.post(self.login_url, data)
        token = login_response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        # Test successful logout
        logout_url = reverse('logout')
        response = self.client.post(logout_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
