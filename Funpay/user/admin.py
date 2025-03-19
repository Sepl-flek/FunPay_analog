from django.contrib import admin
from django.contrib.admin import ModelAdmin

from user.models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class AdminCustomUser(ModelAdmin):
    pass