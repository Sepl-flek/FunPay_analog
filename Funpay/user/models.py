from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    purchases = models.ManyToManyField('Product.Product', through='UserProductRelation')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True
    )


class UserProductRelation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey('Product.Product', on_delete=models.CASCADE)
    in_bookmark = models.BooleanField(default=False)


class UserProductsBought(models.Model):
    pass