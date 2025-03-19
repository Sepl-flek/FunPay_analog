from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from Product.models import Product

User = get_user_model()
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')

class ProductSerializer(ModelSerializer):

    seller = UserSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ('name', 'price', 'category', 'status', 'count', 'seller',)