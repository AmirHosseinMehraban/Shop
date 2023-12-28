from django.contrib.admindocs.utils import docutils_is_available
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


class ProductPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'

class home(APIView):
    pagination_class = ProductPagination

    def get(self, request):
        products = Product.objects.filter(isAvailable=True)

        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(products, request)

        serializer = ProductSerializer(result_page, many=True)
        return Response(serializer.data)