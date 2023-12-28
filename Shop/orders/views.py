from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from home.models import Product
from rest_framework.permissions import AllowAny


class CartView(APIView):
    permission_classes = [AllowAny, ]
    def get(self, request):
        print("rr")
        cart = OrderItem.objects.filter(order__user=request.user)
        serializer = OrderItemSerializer(instance=cart, many=True)
        return Response(serializer.data)

    def post(self, request, product_id):
        #should be change later
        cart, created = Order.objects.get_or_create(user=request.user)
        product = Product.objects.get(pk=product_id)
        cart_item, created = OrderItem.objects.get_or_create(order=cart, product=product)
        serializer = OrderItemSerializer(data=request.POST)
        return Response(serializer.data)

    def delete(self, request, product_id):
        cart = Order.objects.get(user=request.user)
        product = Product.objects.get(pk=product_id)
        cart_item = OrderItem.objects.get(cart=cart, product=product)
        cart_item.delete()
        serializer = OrderSerializer(cart)
        return Response(serializer.data)

