from django.contrib.auth.decorators import login_required
from django.db.models import When
from django.shortcuts import render
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from user.models import UserProductRelation, CustomUser
from user.serializers import UserProductRelationSerializer, ProfileSerializer


class UserProductRelationViewSet(UpdateModelMixin, GenericViewSet):
    serializer_class = UserProductRelationSerializer
    queryset = UserProductRelation.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'product'

    def get_object(self):
        obj, created = UserProductRelation.objects.get_or_create(user=self.request.user,
                                                                 product_id=self.kwargs['product'])

        return obj


class MyUserProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.none()

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id).prefetch_related('products')

    def get_object(self):
        return self.request.user


@login_required
def profile_view(request):
    return render(request, 'profile.html')


def auth(request):
    return render(request, 'auth.html')
