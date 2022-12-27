"""
Products API/Serializer file 
"""
from rest_framework import serializers
from structure.core.base_serializer import BaseSerializer
from structure.inventory.models import (
    Product,
    ProductInventory,
    ProductType,
    Brand,
)


"""
Product Serializer 
"""


class ProductSerializer(BaseSerializer):
    class Meta:
        model = Product
        fields = BaseSerializer.Meta.fields + (
            "name",
            "slug",
            "description",
            "category",
        )


"""
product Inventory Serializer 
"""


class ProductInventorySerializer(BaseSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(is_active=True)
    )
    product_type = serializers.PrimaryKeyRelatedField(
        queryset=ProductType.objects.filter(is_active=True)
    )
    brand = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.filter(is_active=True)
    )

    class Meta:
        model = ProductInventory
        fields = BaseSerializer.Meta.fields + (
            "product",
            "sku",
            "upc",
            "retail_price",
            "regular_price",
            "weight",
            "product_type",
            "brand",
            "attributes",
        )
