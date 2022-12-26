"""
Category serializers
"""

from structure.inventory.models import Category
from structure.core.base_serializer import BaseSerializer


class CategorySerializer(BaseSerializer):
    class Meta:
        model = Category
        fields = BaseSerializer.Meta.fields + ("name", "slug", "parent")
        depth = 1
