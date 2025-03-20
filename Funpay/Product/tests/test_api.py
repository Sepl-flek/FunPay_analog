import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Product.models import Product
from Product.serializers import ProductSerializer
from user.models import CustomUser


class ProductApiTestCase(APITestCase):

    def setUp(self):
        self.user1 = CustomUser.objects.create(username='test1')
        self.user2 = CustomUser.objects.create(username='test2')

        self.product1 = Product.objects.create(seller=self.user1, name='account', price=10, category='account')
        self.product2 = Product.objects.create(seller=self.user1, name='account1', price=20, category='account')
        self.product3 = Product.objects.create(seller=self.user1, name='account2', price=90.9, category='account')

    def test_get(self):
        url = reverse('product-list')

        response = self.client.get(url)
        products = Product.objects.all()
        serializer_data = ProductSerializer(products, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_update(self):
        url = reverse('product-detail', args=(self.product1.pk, ))

        data = {
            'price': 20
        }
        json_data = json.dumps(data)

        self.client.force_login(self.user1)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.product1.refresh_from_db()
        self.assertEqual(20, self.product1.price)

    def test_update_logout(self):
        url = reverse('product-detail', args=(self.product1.pk, ))

        data = {
            'price': 20
        }
        json_data = json.dumps(data)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)


    def test_create(self):
        self.client.force_login(self.user1)
        url = reverse('product-list')

        data = {
            'name': 'test_name',
            'price': 100,
            'category': 'other'
        }
        response = self.client.post(url, data=data)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Product.objects.all().count())
        self.assertEqual(self.user1.username, Product.objects.last().seller.username)