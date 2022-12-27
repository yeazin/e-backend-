"""
Dependency models API 
    Brand
    Product Attribute 
    Product Type
    product Inventory Media
    Stock
    Product Attribute value
    Product Attribute Values
    """

from rest_framework import serializers
from structure.core.base_serializer import BaseSerializer
from structure.inventory.models import (
    Brand,
    ProductAttribute,
    ProductType,
    ProductInventoryMedia,
    Stock,
    ProductAttributeValue,
    ProductAttributeValues,
    ProductInventory,
)

"""
Brand Serializer
"""


class BrandSerializer(BaseSerializer):
    class Meta:
        model = Brand
        fields = BaseSerializer.Meta.fields + ("name",)


"""
Stock Seralizer 
"""


class StockSerializer(BaseSerializer):
    product_inventory = serializers.PrimaryKeyRelatedField(
        queryset=ProductInventory.objects.filter(is_active=True)
    )

    class Meta:
        model = Stock
        fields = BaseSerializer.Meta.fields + (
            "product_inventory",
            "last_checked",
            "units",
            "units_sold",
        )


"""
Product Type Serializer 
"""


class ProductTypeSerializer(BaseSerializer):
    class Meta:
        model = ProductType
        fields = BaseSerializer.Meta.fields + ("name",)


"""
Product Attribute Serializer 
"""


class ProductAttributeSerializer(BaseSerializer):
    class Meta:
        model = ProductAttribute
        fields = BaseSerializer.Meta.fields + (
            "name",
            "description",
        )


"""
Product Attribute Value Serializer 
"""


class ProductAttributeValueSerializer(BaseSerializer):
    attribute = serializers.PrimaryKeyRelatedField(
        queryset=ProductAttribute.objects.filter(is_active=True)
    )

    class Meta:
        model = ProductAttributeValue
        fields = BaseSerializer.Meta.fields + ("attribute", "attribute_value")


"""
Product Attribute Values 
    Link Model serializer for 
    Product inventory and product Attribute 
"""


class LinkProductAttributeValuesSerializer(BaseSerializer):
    product_inventory = serializers.PrimaryKeyRelatedField(
        queryset=ProductInventory.objects.filter(is_active=True)
    )
    attributes = serializers.PrimaryKeyRelatedField(
        queryset=ProductAttributeValue.objects.filter(is_active=True)
    )

    class Meta:
        model = ProductAttributeValues
        fields = BaseSerializer.Meta.fields + ("product_inventory", "attributes")


"""
product Inventory Media Serializers 
"""


class ProductInventoryMediaSerializer(BaseSerializer):
    product_inventory = serializers.PrimaryKeyRelatedField(
        queryset=ProductInventory.objects.filter(is_active=True)
    )

    class Meta:
        model = ProductInventoryMedia
        fields = BaseSerializer.Meta.fields + (
            "product_inventory",
            "title",
            "image",
            "alt_text",
            "is_featured",
        )
