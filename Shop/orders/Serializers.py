from rest_framework import serializers
from .models import OrderItem, Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderItemSelectSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
