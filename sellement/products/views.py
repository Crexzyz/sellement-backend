from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from products.serializers import ProductModelSerializer
from products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    pagination_class = PageNumberPagination
    serializer_class = ProductModelSerializer

    def list(self, request):
        products = Product.objects.all().order_by('id')

        page = self.paginate_queryset(products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
