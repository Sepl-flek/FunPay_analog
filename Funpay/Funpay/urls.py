"""
URL configuration for Funpay project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter

from Product.views import ProductViewSet, product_page
from user.views import UserProductRelationViewSet, auth, MyUserProfileViewSet

router = SimpleRouter()
router.register(r'api/products', ProductViewSet)
router.register(r'api/product_relation', UserProductRelationViewSet)
router.register(r'api/profile', MyUserProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', product_page, name='product_page'),
    re_path('', include('social_django.urls', namespace='social')),
    path('authentication/', auth),
    path('user/', include('user.urls')),
]

urlpatterns += router.urls
