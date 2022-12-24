"""
Inventory Models
"""

from django.db import models
from mainConfig.models.mixin import TimeStampMixin
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


"""
Category models 
"""


class Category(MPTTModel, TimeStampMixin):

    ## Category table implimented with MPTT
    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Category Name"),
        help_text=_("format: required , max-200"),
    )
    slug = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Category Safe URL"),
        help_text=_("format: required , max-200"),
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Product Category"),
        help_text=_("Not Required"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return str(self.name)


"""
Product models
"""


class Product(TimeStampMixin):
    """
    Products tables
    """

    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Prodcut Name"),
        help_text=_("format: required , max-200"),
    )
    slug = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Product Safe URL"),
        help_text=_("format: required , max-255"),
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Product Description"),
        help_text=_("Not required"),
    )
    category = TreeManyToManyField(Category)

    class Meta:
        verbose_name_plural = _("Product Table")

    def __str__(self):
        return self.name


"""
Product Inventory Models. 
    Note : This product inventory models is a version type models 
    for example if we have a product name shoes 
    then there might be chances that product has differenct color and sizes.
    And thats how the Prodcut inventory comes in. 
    We can then spacify the varities of products in this product inventory models 
"""


class ProductInventory(TimeStampMixin):

    """
    Product Inventory Properties
    """

    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="product"
    )
    sku = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_("Stock Keeping UNIT"),
        help_text=_("required, max-30"),
    )
    upc = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_("Universal Product Code"),
        help_text=_("required, max-30"),
    )
    retail_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Retail Price"),
        help_text=_("Format:maximum Price 999.99"),
        error_messages={
            "name": {"max_length": _("the price must be between 0 to 999.99")},
        },
    )
    regular_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Regular Price"),
        help_text=_("Format:maximum Price 999.99"),
        error_messages={
            "name": {"max_length": _("the price must be between 0 to 999.99")},
        },
    )
    weight = models.FloatField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("Product Weight"),
        help_text=_("Format: Not Required"),
    )
