from warehouse.models import SemiFinishedItem
from .models import Cart, Operation
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserApiTest(APITestCase):

    def test_create_user_api(self):
        data = {'username': 'lesio', 'e-mail': 'lesio@mail.com', 'password': 'leszek'}
        url = reverse('user')

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cart.objects.count(), 1)
        user = User.objects.first()
        user_cart = Cart.objects.first()
        self.assertEqual(user_cart.worker, user)

    def test_access_to_user_cart(self):

        data = {'username': 'lesio', 'e-mail': 'lesio@mail.com', 'password': 'leszek'}
        url = reverse('user')
        response = self.client.post(url, data, format='json')
        user = User.objects.first()
        url = reverse('cart-detail', kwargs={'worker__username': user.username})
        payload = payload_handler(user)
        token = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'lesio')

    def test_access_to_foreign_cart(self):
        data = {'username': 'lesio', 'e-mail': 'lesio@mail.com', 'password': 'leszek'}
        data2 = {'username': 'leszek', 'e-mail': 'leszek@mail.com', 'password': 'leszek'}

        url = reverse('user')
        response = self.client.post(url, data, format='json')
        response = self.client.post(url, data2, format='json')

        self.assertEqual(User.objects.count(),2)
        user = User.objects.get(username='lesio')
        url = reverse('cart-detail', kwargs={'worker__username': 'leszek'})
        payload = payload_handler(user)
        token = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_cart(self):
        data = {'username': 'lesio', 'e-mail': 'lesio@mail.com', 'password': 'leszek'}
        url = reverse('user')
        response = self.client.post(url, data, format='json')
        url = reverse('cart-detail', kwargs={'worker__username': 'lesio'})
        user = User.objects.first()
        payload = payload_handler(user)
        token = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        data = {}
        response = self.client.get(url, data, format='json')
        data = response.data
        data['products'] = ["1", "2"]
        data['quantities'] = [1, 2]
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_operation_from_cart(self):
        item_1 = SemiFinishedItem.objects.create(name='Test item', quantity=10, producer='Leszek')
        item_2 = SemiFinishedItem.objects.create(name='Test second item', quantity=10, producer='Leszek')
        item_3 = SemiFinishedItem.objects.create(name='Test third item', quantity=10, producer='Leszek')

        data = {'username': 'lesio', 'e-mail': 'lesio@mail.com', 'password': 'leszek'}
        url = reverse('user')
        response = self.client.post(url, data, format='json')
        url = reverse('cart-detail', kwargs={'worker__username': 'lesio'})
        user = User.objects.first()
        payload = payload_handler(user)
        token = encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        data = {}
        response = self.client.get(url, data, format='json')

        data = response.data
        data['products'] = ["1", "2"]
        data['quantities'] = [1, 2]
        data['operation'] = 'ER'
        response = self.client.patch(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Operation.objects.count(),1)
        operation = Operation.objects.first()
        print(operation.operation_number)
        self.assertEqual(operation.operation_number, 'ER/1/2018')
        self.assertEqual(operation.products, ["1", "2"])

        item_1 = SemiFinishedItem.objects.get(name='Test item')
        item_3 = SemiFinishedItem.objects.get(name='Test third item')

        self.assertEqual(item_1.quantity, 9)
        self.assertEqual(item_3.quantity, 10)

