from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer, CategorySerializer
from .models import Product, Category


class home(APIView):
    def get(self, request):
        product = Product.objects.filter(is_available=True)
        category = Category.objects.all()
        cat_slug = request.GET.get('cat_slug', False)
        if cat_slug:
            category = Category.objects.filter(slug=cat_slug)
            product = Product.objects.filter(category__name=cat_slug)

        cat_ser = CategorySerializer(instance=category, many=True)
        product_ser = ProductSerializer(instance=product, many=True)
        # need attention

        return Response(data={
            "category": cat_ser.data,
            "product": product_ser.data
        })

# Create your views here.
