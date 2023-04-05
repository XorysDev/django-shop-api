from rest_framework import serializers
from .models import OrderItem, Order
from product.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    product_title = serializers.ReadOnlyField(source="product.title")

    class Meta:
        model = OrderItem
        fields = ('product', 'product_title', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    user = serializers.ReadOnlyField(source='user.email')
    products = OrderItemSerializer(write_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        products = validated_data.pop('products')
        request = self.context['requests']
        user = request.user
        total_sum = 0

        for product in products:
            try:
                total_sum += product['quantity'] * product['product'].price
            except KeyError:
                total_sum += product['product'].price

        order = Order.objects.create(user=user, status='open', total_sum=total_sum, **validated_data)


