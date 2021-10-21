from django.db.models import fields
from rest_framework import serializers
from wishlists.models import ItemsOnWishlist, Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = [
            'title',
            'slug',
            'date',
            'user',
        ]

class ItemsOnWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsOnWishlist
        fields = [
            'item',
            'wishlist',
        ]
