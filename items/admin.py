from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from items.models import Item


@admin.register(Item)
class PictureAdmin(ModelAdmin):
    base_model = Item
