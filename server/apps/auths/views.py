from typing import Optional
from datetime import datetime

from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request

from django.db.models import QuerySet

# from abstracts.validators import APIValidator
from auths.models import CustomUser
from auths.serializers import CustomUserSerializer


class CustomUserViewSet(ViewSet):
    """ViewSet for CustomUser."""

    permission_classes: tuple = (
        permissions.AllowAny,
    )
    queryset: QuerySet[CustomUser] = \
        CustomUser.objects.get_not_deleted()

    def get_queryset(self) -> QuerySet[CustomUser]:
        return self.queryset.filter(
            is_superuser=True
        )
