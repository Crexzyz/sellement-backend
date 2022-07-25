from products.serializers import CategoryModelSerializer
from products.serializers import ProductModelSerializer

from products.models import Category
from products.models import Product

from common.viewsets import PaginatedViewSet

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class ProductViewSet(PaginatedViewSet):
    """Provides GET, POST, PUT, and DELETE actions for a single product"""
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()

    def list(self, request):
        """Returns all the products in the database"""
        products = Product.objects.all().order_by('id')
        return super().paginate_data(products)

    @action(detail=False, methods=["GET"])
    def form(self, request):
        return Response(Product.emptyForm(), status.HTTP_200_OK)


class CategoryViewSet(PaginatedViewSet):
    """Provides GET, POST, PUT, and DELETE actions for a single category"""
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()

    def list(self, request):
        """Returns all the categories in the database"""
        categories = Category.objects.all().order_by('name')
        return super().paginate_data(categories)
