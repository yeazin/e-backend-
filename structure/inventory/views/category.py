"""
Category Views 
"""
from rest_framework import generics
from rest_framework import permissions
from structure.inventory.models import Category
from structure.inventory.api.category_api import CategorySerializer


class CategoryList(generics.ListAPIView):
    permission_classes = ()
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
