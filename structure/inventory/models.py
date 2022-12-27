"""
Inventory Models
"""

from django.db import models
from structure.core.base_models import TimeStampMixin
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
        return str(self.name)


"""
Dependeny models of Product Inventory 
"""

## Product Type
class ProductType(TimeStampMixin):
    """
    Product properties
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        verbose_name=_("Product Type"),
        help_text=_("Format: Required and Unique"),
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Product Type"


## Brand
class Brand(TimeStampMixin):
    """
    Brand properties
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        verbose_name=_("Brand Name"),
        help_text=_("Format: Required and Unique"),
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Brand"


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
    product_type = models.ForeignKey(
        ProductType, on_delete=models.PROTECT, null=True, related_name="product_type"
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, null=True, related_name="brand"
    )
    attributes = models.ManyToManyField(
        "inventory.ProductAttributeValue",
        related_name="product_attribute_values",
        through="ProductAttributeValues",
    )

    def __str__(self):
        return "Product : {} , Type : {}".format(self.product, self.product_type)

    class Meta:
        verbose_name_plural = "Product Inventory"


"""
Product Media models 
"""


class ProductInventoryMedia(TimeStampMixin):
    """
    Product Inventory image properties
    """

    product_inventory = models.ForeignKey(
        ProductInventory,
        null=True,
        on_delete=models.PROTECT,
        related_name="media_product_inventory",
    )
    title = models.CharField(
        max_length=255,
        unique=False,
        verbose_name=_("Product Image Title"),
        help_text=_("Format : Required"),
    )
    image = models.ImageField(
        unique=False,
        blank=False,
        verbose_name=_("Product Image"),
        help_text=_("Format : required"),
        upload_to="images/product/",
    )
    alt_text = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Alt Text"),
        help_text=_("format : Not Required"),
    )
    is_featured = models.BooleanField(
        default=False,
        verbose_name=_("Is Featured ?"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Inventory Images"


"""
Stock models 
    Note : This models is created for tracking the stock/quantity for 
    Product Inventory
"""


class Stock(TimeStampMixin):
    """
    Product Stock properties
    """

    product_inventory = models.OneToOneField(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name="product_inventory_stock",
    )
    last_checked = models.DateTimeField(
        unique=False,
        blank=True,
        null=True,
        verbose_name=_("Last Inventory Stock Checked"),
        help_text=_("Format : Not Required"),
    )
    units = models.IntegerField(
        default=0,
        unique=False,
        verbose_name=_("Product Unit/stock"),
        help_text=_("Format : Default 0"),
    )
    units_sold = models.IntegerField(
        default=0,
        unique=False,
        verbose_name=_("Product Unit/stock sold"),
        help_text=_("Format : Default 0"),
    )

    def __str__(self):
        return "Product : {}, In Stock : {} , Sold : {}".format(
            self.product_inventory, self.units, self.units_sold
        )

    class Meta:
        verbose_name_plural = "Product Inventory Stock"


"""
Prodcut Attributes models and Dependency 
"""

## product Attribute models
class ProductAttribute(TimeStampMixin):
    """
    Attributes properties
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        verbose_name=_("Attribute Name"),
        help_text=_("Format : Should Be unique"),
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Attribute Description"),
        help_text=_("Format : Not Required"),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Product Attribute"


## Product Attribute Value models
class ProductAttributeValue(TimeStampMixin):
    """
    Attribute values properties
    """

    attribute = models.ForeignKey(
        ProductAttribute,
        on_delete=models.PROTECT,
        null=True,
        related_name="product_attribute",
        verbose_name=_("Attribute Name"),
        help_text=_("Format : Required"),
    )
    attribute_value = models.CharField(
        max_length=255,
        unique=False,
        blank=False,
        verbose_name=_("Attribute Value Name"),
        help_text=_("Format : max 255 character"),
    )

    def __str__(self):
        return "Attribute Name : {} , Value : {}".format(
            self.attribute, self.attribute_value
        )

    class Meta:
        verbose_name_plural = "Product Attribute Value"


## Product Attribute Values
class ProductAttributeValues(TimeStampMixin):
    """
    Product link to Attribute values
    through models
    """

    product_inventory = models.ForeignKey(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name="inventory_values",
        null=True,
    )
    attributes = models.ForeignKey(
        ProductAttributeValue,
        on_delete=models.PROTECT,
        null=True,
        related_name="attribute_values",
    )

    def __str__(self):
        return "Product Inventory : {}, Attributes : {}".format(
            self.product_inventory, self.attributes
        )

    class Meta:
        unique_together = ("product_inventory", "attributes")
