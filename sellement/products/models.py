from django.db import models


class Category(models.Model):
    """Represents the category of one or more products"""
    name = models.CharField(max_length=30, primary_key=True)

    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    """Represents a product in stock"""
    # Id added automatically
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    stock = models.IntegerField(default=0)
    purchase_price = models.FloatField(default=0.0)
    sell_price = models.FloatField(default=0.0)
    date_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self) -> str:
        return self.name
