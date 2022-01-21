from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError
from products.models import Category
from products.models import Product


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate(self, data):
        numeric_fields = ['stock', 'purchase_price', 'sell_price']

        for field in numeric_fields:
            if data[field] >= 0.0:
                continue
            raise ValidationError({field: "This value can not be negative"})
        return data


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
