from products.serializers import (
    CategoryModelSerializer,
    ProductModelSerializer
)

from products.models import Category, Product
from common.viewsets import PaginatedViewSet


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
