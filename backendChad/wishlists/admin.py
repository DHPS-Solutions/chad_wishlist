from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from wishlists.models import Wishlist


@admin.register(Wishlist)
class PictureAdmin(ModelAdmin):
    base_model = Wishlist