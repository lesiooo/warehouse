from .models import SemiFinishedItem
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER


class SemiFinishedItemAPITest(APITestCase):

    def setUp(self):
        super(SemiFinishedItemAPITest, self).setUp()
        self.user = User.objects.create_user('lesio', 'leiso@mail.com', 'leszek')
        self.item = SemiFinishedItem.objects.create(name='Test item', quantity=123, producer='Test producer')


    def test_get_api_semi_finished_items_list(self):
        data = {}
        url = reverse('semi-finished-item-list')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test item')

    def test_post_api_sfi(self):
        data = {'name': 'Test post item', 'quantity': 56, 'producer': 'Leszek'}
        url = reverse('semi-finished-item-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_api_item_with_login_user(self):
        data = {'name': 'Test post item', 'quantity': 56, 'producer': 'Leszek'}
        url = reverse('semi-finished-item-list')

        user = User.objects.first()
        payload = payload_handler(user)
        token = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SemiFinishedItem.objects.count(), 2)
        #self.assertContains(response, 'Test item')
        #self.assertContains(response, 'Test post item')

    def test_update_quantity_item(self):
        item = SemiFinishedItem.objects.first()
        data = {'name': 'Test updated item', 'quantity': 125, 'producer': 'Test producer'}
        url = item.get_absolute_url()

        user = User.objects.first()
        payload = payload_handler(user)
        token = encode_handler(payload)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 401)

        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        item = SemiFinishedItem.objects.first()
        self.assertEqual(item.name, 'Test updated item')
        self.assertEqual(item.quantity, 125)

    def test_delete_item(self):
        item = SemiFinishedItem.objects.first()
        url = item.get_absolute_url()

        user = User.objects.first()
        payload = payload_handler(user)
        token = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(SemiFinishedItem.objects.count(), 0)
