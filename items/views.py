from rest_framework import viewsets

from items.models import Item
from items.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
