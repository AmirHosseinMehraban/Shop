from django.contrib.admindocs.utils import docutils_is_available
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

class home(APIView):
    pagination_class = ProductPagination

    def get(self, request, category=None):
        print("*"*99)
        print(request.user)
        search_query = request.GET.get('search', '')
        if category:
            products = Product.objects.filter(isAvailable=True, name__icontains=search_query, category__name=category)
        else :
            products = Product.objects.filter(isAvailable=True, name__icontains=search_query)

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, name):
        product = Product.objects.get(name=name)
        product_srz = ProductSerializer(product)
        return Response(data=product_srz.data, status=200)


    def post(self, request, name):
        product = Product.objects.get(name=name)
        product_srz = ProductSerializer(product)
        return Response(data=product_srz.data)








