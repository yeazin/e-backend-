"""
Products Views 
"""
from rest_framework import generics
from structure.inventory.models import Product, ProductInventory
from structure.inventory.api.products_api import (
    ProductSerializer,
    ProductInventorySerializer,
)


"""
Products LIst View 
Create view 
"""


class ProductsListCreate(generics.ListCreateAPIView):
    permission_classes = ()
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer


"""
Product
    Retrieve View
    Update View 
    Delete view 
"""


class ProductSingle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer


"""
Product Inventory 
    List View
    create View 
"""


class ProductInventoryListCreate(generics.ListCreateAPIView):
    permission_classes = ()
    queryset = ProductInventory.objects.filter(is_active=True)
    serializer_class = ProductInventorySerializer


"""
Product Inventory 
    Single View
    Update View
    Delete View 
"""


class SingleProductInventory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    queryset = ProductInventory.objects.filter(is_active=True)
    serializer_class = ProductInventorySerializer
