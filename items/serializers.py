from rest_framework import serializers

from items.models import Item


class ItemSerializer(serializers.Serializer):
    class Meta:
        model = Item
        fields = [
            'name',
            'price',
        ]
