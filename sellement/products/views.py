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

    @action(detail=False, methods=["GET"], url_path="form")
    def emptyForm(self, request):
        # TODO: Create generic class that automatically adds this form
        # functions, like ModelViewSet
        "Returns the empty form that should be presented to create a Product"
        return Response(Product.emptyForm(), status.HTTP_200_OK)

    @action(detail=True, methods=["GET"])
    def form(self, request, pk):
        """Returns the model's form of an existing Product instance"""
        form: dict = {}
        statusCode = status.HTTP_200_OK
        try:
            product: Product = Product.objects.get(pk=pk)
            form = product.form()
        except Product.DoesNotExist:
            statusCode = status.HTTP_404_NOT_FOUND
            form["error"] = "Product does not exist"

        return Response(form, statusCode)


class CategoryViewSet(PaginatedViewSet):
    """Provides GET, POST, PUT, and DELETE actions for a single category"""
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()

    def list(self, request):
        """Returns all the categories in the database"""
        categories = Category.objects.all().order_by('name')
        return super().paginate_data(categories)
