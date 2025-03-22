from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from Product.models import Product
from user.models import UserProductRelation

User = get_user_model()


class ProductUserSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price', 'category', 'status', 'count')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class ProfileSerializer(ModelSerializer):
    products = ProductUserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'balance', 'products')


class UserProductRelationSerializer(ModelSerializer):
    class Meta:
        model = UserProductRelation
        fields = ('product', 'in_bookmark', 'rating')
