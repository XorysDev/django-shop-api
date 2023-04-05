from rest_framework import serializers
from .models import OrderItem, Order
from product.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    product_title = serializers.ReadOnlyField(source="product.title")

    class Meta:
        model = OrderItem
        fields = ('product', 'product_title', 'quantity')

