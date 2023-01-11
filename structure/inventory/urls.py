"""
Inventory APP URLs 
"""

from django.urls import path
from structure.inventory.views.category import CategoryList, SingleCategory
from structure.inventory.views.products import (
    ProductsListCreate,
    ProductSingle,
    ProductInventoryListCreate,
    SingleProductInventory,
)
from structure.inventory.views.dependency_view import (
    BrandListCreate,
    SingleBrand,
    StockListCreate,
    SingleStock,
    ProductTypeListCreate,
    SingleProductType,
    ProductAttributeListCreate,
    SingleProductAttribute,
    productAttributeValueListCreate,
    SingleProductAttributeValue,
    ProductAttributeValuesListCreate,
    SingleProductAttributeValues,
    ProductInventoryMediaListCreate,
    SingleProductInventoryMedia,
)

urlpatterns = []

category_URL = [
    path("category/", CategoryList.as_view()),
    path("category/<uuid:pk>/", SingleCategory.as_view(), name="c"),
]

product_URL = [
    path("product/", ProductsListCreate.as_view()),
    path("product/<uuid:pk>/", ProductSingle.as_view()),
    path("product/inventory/", ProductInventoryListCreate.as_view()),
    path("product/inventory/<uuid:pk>/", SingleProductInventory.as_view()),
]

dependency_URL = [
    path("brand/", BrandListCreate.as_view()),
    path("brand/<uuid:pk>/", SingleBrand.as_view()),
    path("stock/", StockListCreate.as_view()),
    path("stock/<uuid:pk>/", SingleStock.as_view()),
    path("product-type/", ProductTypeListCreate.as_view()),
    path("product-type/<uuid:pk>/", SingleProductType.as_view()),
    path("attribute/", ProductAttributeListCreate.as_view()),
    path("attribute/<uuid:pk>/", SingleProductAttribute.as_view()),
    path("attribute-value/", productAttributeValueListCreate.as_view()),
    path("attribute-value/<uuid:pk>/", SingleProductAttributeValue.as_view()),
    path("link-attribute-value/", ProductAttributeValuesListCreate.as_view()),
    path("link-attribute-value/<uuid:pk>/", SingleProductAttributeValues.as_view()),
    path("inventory/media/", ProductInventoryMediaListCreate.as_view()),
    path("inventory/media/<uuid:pk>/", SingleProductInventoryMedia.as_view()),
]

urlpatterns += category_URL
urlpatterns += product_URL
urlpatterns += dependency_URL
