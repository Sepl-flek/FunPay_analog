from django.shortcuts import render
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from Product.models import Product
from Product.permission import IsOwnerOrReadOnly
from Product.serializers import ProductSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering_fields = ['name', 'price', 'count']

    def perform_create(self, serializer):
        serializer.validated_data['seller'] = self.request.user
        serializer.save()


def product_page(request):
    return render(request, 'products.html')


def information_about_product(request, pk):
    return render(request, 'product.html')
