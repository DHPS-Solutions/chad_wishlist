from rest_framework import serializers
from wishlists.models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = [
            'title',
            'slug',
            'date',
            'user',
        ]
