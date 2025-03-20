import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Product.models import Product
from user.models import CustomUser, UserProductRelation


class ProductRelationApiTestCase(APITestCase):

    def setUp(self):
        self.user1 = CustomUser.objects.create(username='test1')
        self.user2 = CustomUser.objects.create(username='test2')

        self.product1 = Product.objects.create(seller=self.user1, name='account', price=10, category='account')
        self.product2 = Product.objects.create(seller=self.user1, name='account1', price=20, category='account')
        self.product3 = Product.objects.create(seller=self.user1, name='account2', price=90.9, category='account')

    def test_bookmark(self):
        url = reverse('userproductrelation-detail', args=(self.product1.pk,))
        data = {
            'in_bookmark': True
        }
        json_data = json.dumps(data)
        self.client.force_login(self.user1)
        response = self.client.patch(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        relation = UserProductRelation.objects.get(user=self.user1, product=self.product1)
        self.assertTrue(relation.in_bookmark)
