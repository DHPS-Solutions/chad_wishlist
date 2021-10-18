from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Wishlist(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


