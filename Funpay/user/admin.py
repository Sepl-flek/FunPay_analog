from django.contrib import admin
from django.contrib.admin import ModelAdmin

from user.models import CustomUser, UserProductRelation


# Register your models here.
@admin.register(CustomUser)
class AdminCustomUser(ModelAdmin):
    pass


@admin.register(UserProductRelation)
class AdminUserProductRelation(ModelAdmin):
    pass
