from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from Product.models import Product
from user.serializers import UserSerializer


class ProductSerializer(ModelSerializer):
    seller = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'price', 'category', 'status', 'count', 'seller',)
