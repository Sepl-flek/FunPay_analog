from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from Product.models import Product
from Product.serializers import ProductSerializer


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().select_related('seller')
    serializer_class = ProductSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]


def product_page(request):
    return render(request, 'products.html')