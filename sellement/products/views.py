from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from products.serializers import (
    CategoryModelSerializer,
    ProductModelSerializer
)

from products.models import Category, Product


class PaginatedViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination
    serializer_class = None

    def paginate_data(self, data):
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)


class ProductViewSet(PaginatedViewSet):
    serializer_class = ProductModelSerializer

    def list(self, request):
        products = Product.objects.all().order_by('id')
        return super().paginate_data(products)


class CategoryViewSet(PaginatedViewSet):
    serializer_class = CategoryModelSerializer

    def list(self, request):
        categories = Category.objects.all().order_by('name')
        return super().paginate_data(categories)
