from django.shortcuts import render
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from Product.models import Product
from Product.permission import IsOwnerOrReadOnly
from Product.serializers import ProductSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['seller'] = self.request.user
        serializer.save()


def product_page(request):
    return render(request, 'products.html')
