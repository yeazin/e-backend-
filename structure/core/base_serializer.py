"""
Base Serializer 
"""

from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "is_active", "created_at", "updated_at")
        abstract = True
