from django.urls import path
from .views import profile_view, auth

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('login/', auth),
]
