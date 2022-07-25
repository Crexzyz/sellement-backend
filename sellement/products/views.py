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

    @action(detail=False, methods=["GET"], url_path='form/(?P<pk>[^/.]+)')
    def form(self, request, pk=None):
        """Returns the model's form. If given with a primary key, it
        will return the data of the selected instance"""
        form: dict = {}
        statusCode = status.HTTP_200_OK

        if pk is not None:
            try:
                product: Product = Product.objects.get(pk=pk)
                form = product.form()
            except Product.DoesNotExist:
                statusCode = status.HTTP_404_NOT_FOUND
                form["error"] = "Product does not exist"
        else:
            form = Product.emptyForm()

        return Response(form, statusCode)


class CategoryViewSet(PaginatedViewSet):
    """Provides GET, POST, PUT, and DELETE actions for a single category"""
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()

    def list(self, request):
        """Returns all the categories in the database"""
        categories = Category.objects.all().order_by('name')
        return super().paginate_data(categories)
