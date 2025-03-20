from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from user.models import UserProductRelation

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')


class UserProductRelationSerializer(ModelSerializer):
    class Meta:
        model = UserProductRelation
        fields = ('product', 'in_bookmark')
