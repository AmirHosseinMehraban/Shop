from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializers import OrderSerializer, OrderItemSerializer, OrderItemSelectSerializer
from .models import Order, OrderItem
from home.models import Product
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404


class CartView(APIView):
    permission_classes = [AllowAny, ]
    def get(self, request):
        print("rr")
        cart = OrderItem.objects.filter(order__user=request.user)
        serializer = OrderItemSerializer(instance=cart, many=True)
        return Response(serializer.data)

    def post(self, request, product_id):
        cart, created = Order.objects.get_or_create(user=request.user)
        product = Product.objects.get(pk=product_id)
        serializer = OrderItemSelectSerializer(data=request.POST)
        if serializer.is_valid():
            if OrderItem.objects.filter(order=cart, product=product).exists():
                cart_item = OrderItem.objects.get(order=cart, product=product)
                quantity = cart_item.quantity
                print(cart_item.quantity)
                quantity += serializer.data['quantity']
                cart_item.quantity = quantity
                cart_item.save()
                print(cart_item)
            else:
                cart_item = OrderItem.objects.get_or_create(order=cart, product=product, price=product.price,
                                                            quantity=serializer.data['quantity'])

        return Response(serializer.data)

    def delete(self, request, order_id):
        cart = OrderItem.objects.filter(order__user=request.user)
        order = OrderItem.objects.get(id=order_id)
        order.delete()
        serializer = OrderItemSerializer(instance=cart, many=True)
        return Response(serializer.data)

class BuyView(APIView):
    def post(self, request, order_id):
        cart = get_object_or_404(Order, id=order_id)
        cart.delete()
        return Response({"message": "you buy successfully"})


