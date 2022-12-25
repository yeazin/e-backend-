from django.contrib import admin
from structure.inventory.models import (
    Category,
    Product,
    Brand,
    ProductType,
    ProductInventory,
)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(ProductType)
admin.site.register(ProductInventory)
