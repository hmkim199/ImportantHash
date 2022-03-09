from backend.apps.user.models import User
from django.urls import reverse
from rest_framework import status

# from rest_framework_simplejwt.models import TokenUser
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class RegisterTestCase(APITestCase):
    def test_register(self):
        data = {
            "user_ID": "testcase",
            "email": "testcase@example.com",
            "password": "NewPassword123",
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
