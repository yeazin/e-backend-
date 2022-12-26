"""
Category serializers
"""
from rest_framework import serializers
from structure.inventory.models import Category
from structure.core.base_serializer import BaseSerializer


class CategorySerializer(BaseSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.filter(is_active=True)
    )

    class Meta:
        model = Category
        fields = BaseSerializer.Meta.fields + ("name", "slug", "parent")
