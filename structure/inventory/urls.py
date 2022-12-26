"""
Inventory URLs 
"""

from django.urls import path
from structure.inventory.views.category import CategoryList, SingleCategory

urlpatterns = [
    path("category/", CategoryList.as_view()),
    path("category/<uuid:pk>/", SingleCategory.as_view()),
]
