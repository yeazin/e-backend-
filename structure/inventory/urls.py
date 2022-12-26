"""
Inventory URLs 
"""

from django.urls import path
from structure.inventory.views.category import CategoryList

urlpatterns = [path("category/", CategoryList.as_view())]
