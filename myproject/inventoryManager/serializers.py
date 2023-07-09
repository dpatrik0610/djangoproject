from rest_framework import serializers
from inventoryManager.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('item_id', 'name', 'value')