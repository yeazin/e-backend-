"""
Category Views 
"""
from rest_framework import generics, status

from rest_framework.response import Response
from structure.inventory.models import Category
from structure.inventory.api.category_api import CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    permission_classes = ()
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        category_obj = CategorySerializer(data=request.data)
        if category_obj.is_valid(raise_exception=True):
            category_obj.save()
            return Response(category_obj.data, status=status.HTTP_201_CREATED)


"""
Single View, update, Delete view
"""


class SingleCategory(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
