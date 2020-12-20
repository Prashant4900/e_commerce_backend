from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'product_name', 'total_product', 'transaction_id', 'total_amount', 'create_at', 'update_at')
