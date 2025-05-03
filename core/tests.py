from django.test import TestCase
from . import models
from django.urls import reverse
from rest_framework import status


class ClientsTestCase(TestCase):
    def setUp(self):
        models.User.objects.create(username="admin", password="admin", is_staff=True)
        models.User.objects.create(username="regular", password="regular", is_staff=False)

    def test_clients_endpoint_list_admin_access(self):
        admin_user = models.User.objects.get(username="admin")
        self.client.force_login(user=admin_user)
        response = self.client.get(reverse("client-view-create"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_clients_endpoint_create_user_admin(self):
        admin_user = models.User.objects.get(username="admin")
        self.client.force_login(admin_user)
        response = self.client.post(reverse("client-view-create"), {"username": "test"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_clients_endpoint_list_non_admin_user_forbidden(self):
        non_admin_authenticated_user = models.User.objects.get(username="regular")
        self.client.force_login(user=non_admin_authenticated_user)
        response = self.client.get(reverse("client-view-create"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_clients_endpoint_create_user_non_admin_user_forbidden(self):
        non_admin_authenticated_user = models.User.objects.get(username="regular")
        self.client.force_login(user=non_admin_authenticated_user)
        response = self.client.post(reverse("client-view-create"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_clients_endpoint_list_unauthenticated_user_unauthorized(self):
        response = self.client.get(reverse("client-view-create"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_clients_endpoint_create_user_unauthenticated_user_unauthorized(self):
        response = self.client.post(reverse("client-view-create"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
