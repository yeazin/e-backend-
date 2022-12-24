"""
Acccounts App serializer 
"""

from rest_framework import serializers
from structure.accounts.models.base import User
from django.contrib.auth.hashers import make_password


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
