from django.db import models
from django.contrib.auth.models import User

from items.models import Item

# Create your models here.

class Wishlist(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

class ItemsOnWishlist(models.Model):

    item = models.ForeignKey(Item, on_delete=models.RESTRICT, default=None)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.RESTRICT, default=None)