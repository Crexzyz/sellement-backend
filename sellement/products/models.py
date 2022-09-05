from django.db import models

from common.form_fields.text_field import TextField
from common.form_fields.currency_field import CurrencyField
from common.form_fields.number_field import NumberField
from common.form_fields.textarea_field import TextareaField


class Category(models.Model):
    NAME_MAX_LENGTH = 30

    """Represents the category of one or more products"""
    name = models.CharField(max_length=NAME_MAX_LENGTH, primary_key=True)

    class Meta:
        verbose_name_plural = "categories"

    def form(self) -> dict:
        return Category.emptyForm(self.name)

    def emptyForm(name_val="") -> dict:
        name = TextField(name_val, "name", "Name", 0, Category.NAME_MAX_LENGTH)
        fields = [name]
        return {"fields": [field.toDict() for field in fields]}


class Product(models.Model):
    """Represents a product in stock"""
    NAME_MAX_LENGTH = 50
    DESCRIPTION_MAX_LENGTH = 300
    # Id added automatically
    name = models.CharField(max_length=50, verbose_name="Name")
    description = models.CharField(max_length=300)
    stock = models.IntegerField(default=0)
    purchase_price = models.DecimalField(default=0.0, decimal_places=4,
                                         max_digits=19)
    sell_price = models.DecimalField(default=0.0, decimal_places=4,
                                     max_digits=19)
    date_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, blank=True)

    def __str__(self) -> str:
        return self.name

    def form(self) -> dict:
        return Product.emptyForm(
            self.pk, self.name, self.description, self.stock,
            self.purchase_price, self.sell_price
        )

    def emptyForm(id_val=None, name_val="", desc_val="", stock_val=0,
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

        if id_val is not None:
            id = TextField(id_val, "id", "id", 4, Product.NAME_MAX_LENGTH,
                           hidden=True, required=True)
            fields.append(id)
        return {
            "fields": [field.toDict() for field in fields]
        }
