"""
Inventory URLs 
"""

from django.urls import path
from structure.inventory.views.category import CategoryList, SingleCategory
from structure.inventory.views.products import (
    ProductsListCreate,
    ProductSingle,
    ProductInventoryListCreate,
    SingleProductInventory,
)

urlpatterns = []

category_URL = [
    path("category/", CategoryList.as_view()),
    path("category/<uuid:pk>/", SingleCategory.as_view()),
]

product_URL = [
    path("product/", ProductsListCreate.as_view()),
    path("product/<uuid:pk>/", ProductSingle.as_view()),
    path("product/inventory/", ProductInventoryListCreate.as_view()),
    path("product/inventory/<uuid:pk>/", SingleProductInventory.as_view()),
]

urlpatterns += category_URL
urlpatterns += product_URL
