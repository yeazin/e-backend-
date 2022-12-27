"""
Dependency models view 
"""
from rest_framework import generics
from structure.inventory.models import (
    Brand,
    ProductAttribute,
    ProductType,
    ProductInventoryMedia,
    Stock,
    ProductAttributeValue,
    ProductAttributeValues,
)
from structure.inventory.api.dependency_api import (
    BrandSerializer,
    ProductTypeSerializer,
    StockSerializer,
    ProductInventoryMediaSerializer,
    ProductAttributeSerializer,
    ProductAttributeValueSerializer,
    LinkProductAttributeValuesSerializer,
)

"""
Brand Views 
    List View,
    Create View,
    Update View,
    Single View ,
    Delete View
"""


class BrandListCreate(generics.ListCreateAPIView):
    permission_classes = ()
    serializer_class = BrandSerializer
    queryset = Brand.objects.filter(is_active=True)


class SingleBrand(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    serializer_class = BrandSerializer
    queryset = Brand.objects.filter(is_active=True)


"""
Stock Views 
    List View,
    Create View,
    Update View,
    Single View ,
    Delete View
"""


class StockListCreate(generics.ListCreateAPIView):
    permission_classes = ()
    serializer_class = StockSerializer
    queryset = Stock.objects.filter(is_active=True)


class SingleStock(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    serializer_class = StockSerializer
    queryset = Stock.objects.filter(is_active=True)


"""
Product Type Views
    List View,
    Create View,
    Update View,
    Single View ,
    Delete View
"""


class ProductTypeListCreate(generics.ListCreateAPIView):
    permission_classes = ()
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.filter(is_active=True)


class SingleProductType(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.filter(is_active=True)


"""
Product Attribute Views
    List View,
    Create View,
    Update View,
    Single View ,
    Delete View
"""


class ProductAttributeListCreate(generics.ListCreateAPIView):
    permission_classes = ()
    serializer_class = ProductAttributeSerializer
    queryset = ProductAttribute.objects.filter(is_active=True)


class SingleProductAttribute(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    serializer_class = ProductAttributeSerializer
    queryset = ProductAttribute.objects.filter(is_active=True)


"""
Product Attribute Value Views
    List View,
    Create View,
    Update View,
    Single View ,
    Delete View
"""


class productAttributeValueListCreate(generics.ListCreateAPIView):
    permission_classes = ()
    serializer_class = ProductAttributeValueSerializer
    queryset = ProductAttributeValue.objects.filter(is_active=True)


class SingleProductAttributeValue(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    serializer_class = ProductAttributeValueSerializer
    queryset = ProductAttributeValue.objects.filter(is_active=True)


"""
Product Attribute Values View
    List View,
    Create View,
    Update View,
    Single View ,
    Delete View
"""


class ProductAttributeValuesListCreate(generics.ListCreateAPIView):
    permission_classes = ()
    serializer_class = LinkProductAttributeValuesSerializer
    queryset = ProductAttributeValues.objects.filter(is_active=True)


class SingleProductAttributeValues(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    serializer_class = LinkProductAttributeValuesSerializer
    queryset = ProductAttributeValues.objects.filter(is_active=True)


"""
Product inventory Media view 
    List View,
    Create View,
    Update View,
    Single View ,
    Delete View
"""


class ProductInventoryMediaListCreate(generics.ListCreateAPIView):
    permission_classes = ()
    serializer_class = ProductInventoryMediaSerializer
    queryset = ProductInventoryMedia.objects.filter(is_active=True)


class SingleProductInventoryMedia(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    serializer_class = ProductInventoryMediaSerializer
    queryset = ProductInventoryMedia.objects.filter(is_active=True)
