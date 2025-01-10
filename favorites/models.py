from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class Favorites(models.Model):

    products = models.ManyToManyField(Product, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    date_added = models.DateField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return f"{self.user.username}'s Favorites"
