from rest_framework import viewsets

from wishlists.models import Wishlist
from wishlists.serializers import WishlistSerializer


class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()