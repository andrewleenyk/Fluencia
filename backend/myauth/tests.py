from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class AuthTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_register(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser2',
            'password1': 'testpass123',
            'password2': 'testpass123',
        })
        self.assertEqual(response.status_code, 302) # 302 status code means redirection, which is what happens after a successful registration.

    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302) # 302 status code means redirection, which is what happens after a successful login.

    def test_logout(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302) # 302 status code means redirection, which is what happens after a successful logout.
