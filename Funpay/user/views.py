from django.shortcuts import render
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from user.models import UserProductRelation
from user.serializers import UserProductRelationSerializer


class UserProductRelationViewSet(UpdateModelMixin, GenericViewSet):
    serializer_class = UserProductRelationSerializer
    queryset = UserProductRelation.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'product'

    def get_object(self):
        obj, created = UserProductRelation.objects.get_or_create(user=self.request.user,
                                                                 product_id=self.kwargs['product'])

        return obj
