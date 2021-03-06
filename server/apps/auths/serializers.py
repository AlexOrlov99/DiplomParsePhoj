from asyncore import read
from dataclasses import field
from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    EmailField,
    BooleanField,
    DateTimeField
)
from auths.models import CustomUser

class CustomUserSerializer(ModelSerializer):
    """CustomuserSerializer"""

    id = IntegerField(read_only=True)
    email = EmailField(read_only=True)
    is_active = BooleanField(read_only=True)
    is_staff = BooleanField(read_only=True)


    class Meta:
        model = CustomUser
        fields =(
            'id',
            'email',
            'is_active',
            'is_staff',
        )