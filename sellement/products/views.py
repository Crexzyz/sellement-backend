from products.serializers import CategoryModelSerializer
from products.serializers import ProductModelSerializer

from products.models import Category
from products.models import Product

from common.viewsets import PaginatedViewSet


class ProductViewSet(PaginatedViewSet):
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()

    def list(self, request):
        products = Product.objects.all().order_by('id')
        return super().paginate_data(products)


class CategoryViewSet(PaginatedViewSet):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()

    def list(self, request):
        categories = Category.objects.all().order_by('name')
        return super().paginate_data(categories)
