from django.db import models

from common.form_fields.text_field import TextField
from common.form_fields.currency_field import CurrencyField
from common.form_fields.number_field import NumberField
from common.form_fields.textarea_field import TextareaField


class Category(models.Model):
    """Represents the category of one or more products"""
    name = models.CharField(max_length=30, primary_key=True)

    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    """Represents a product in stock"""
    NAME_MAX_LENGTH = 50
    DESCRIPTION_MAX_LENGTH = 300
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

    def form(self) -> dict:
        return Product.emptyForm(self.name, self.description, self.stock,
                                 self.purchase_price, self.sell_price)

    def emptyForm(name_val="", desc_val="", stock_val=0,
                  purchase_price_val=0.0, sell_price_val=0.0) -> dict:
        name = TextField(name_val, "name", "Product name", 0,
                         Product.NAME_MAX_LENGTH)
        description = TextareaField(desc_val, "description", "Description", 1,
                                    Product.DESCRIPTION_MAX_LENGTH, 4)
        stock = NumberField(stock_val, "stock", "Stock", 2, 0)
        # TODO: Get currency symbol from database
        purchase_price = CurrencyField(purchase_price_val, "purchase_price",
                                       "Purchase price", 2, 0, "₡")
        sell_price = CurrencyField(sell_price_val, "sell_price", "Sell price",
                                   3, 0, "₡")
        # TODO: Allow categories as an input

        fields = [name, description, stock, purchase_price, sell_price]
        return {
            "fields": [field.toDict() for field in fields]
        }
