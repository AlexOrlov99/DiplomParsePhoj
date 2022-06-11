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

    # @action(
    #     methods=['post'],
    #     detail=False,
    #     url_path='my-custom-endpoint',
    #     permission_classes=(
    #         permissions.AllowAny,
    #     )
    # )
    # def my_custom_endpoint(
    #     self,
    #     request: DRF_Request
    # ) -> DRF_Response:
    #     """Handles POST-request to show custom-info about custom_users."""
    #     serializer: CustomUserSerializer = \
    #         CustomUserSerializer(
    #             self.get_queryset(),
    #             many=True
    #         )
    #     data: list = [
    #         user.id for user in self.get_queryset()
    #     ]
    #     return DRF_Response(
    #         serializer.data
    #     )

    def list(self, request: DRF_Request) -> DRF_Response:
        """Handles GET-request to show custom_users."""

        serializer: CustomUserSerializer = \
            CustomUserSerializer(
                self.get_queryset(),
                many=True
            )
        return DRF_Response(
            serializer.data
        )

    # def create(self, request: DRF_Request) -> DRF_Response:
    #     """Handles POST-request to show custom_users."""

    #     serializer: CustomUserSerializer = \
    #         CustomUserSerializer(
    #             data=request.data
    #         )
    #     if serializer.is_valid():

    #         serializer.save()

    #         return DRF_Response(
    #             f'Объект {serializer.id} создан'
    #         )
    #     return DRF_Response(
    #         'Объект не создан'
    #     )

    # def retrieve(self, request: DRF_Request, pk: int = 0) -> DRF_Response:
    #     """Handles GET-request with ID to show custom_user."""

    #     # Retrieving certain object
    #     #
    #     custom_user: Optional[CustomUser] = None
    #     try:
    #         custom_user = self.get_queryset().get(
    #             id=pk
    #         )
    #     except CustomUser.DoesNotExist:
    #         return self.get_json_response(
    #             'Не нашел такого юзера'
    #         )
    #     serializer: CustomUserSerializer = \
    #         CustomUserSerializer(
    #             custom_user
    #         )
    #     return DRF_Response(
    #         serializer.data
    #     )

    # def partial_update(
    #     self,
    #     request: DRF_Request,
    #     pk: int = 0
    # ) -> DRF_Response:
    #     """Handles PATCH-request with ID to show custom_user."""


    # def update(self, request: DRF_Request) -> DRF_Response:
    #     """Handles PUT-request with ID to show custom_user."""

    # def destroy(self, request: DRF_Request, pk: int = 0) -> DRF_Response:
    #     """Handles DELETE-request with ID to show custom_user."""

    #     custom_user: Optional[CustomUser] = None
    #     try:
    #         custom_user = self.get_queryset().get(
    #             id=pk
    #         )
    #     except CustomUser.DoesNotExist:
    #         return DRF_Response(
    #             f'Объект с ID: {pk} не найден'
    #         )

    #     custom_user.datetime_deleted = datetime.now()
    #     custom_user.save(
    #         update_fields=['datetime_deleted']
    #     )
    #     return DRF_Response(
    #         f'Объект {custom_user.id} удален'
    #     )