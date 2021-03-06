from django.db.models import QuerySet

from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request as DRF_Request
from rest_framework.response import Response as DRF_Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rezume.models import (
    Rezume,
    )
from rezume.serializers import (
    ResumeSerializer, 
    FileSerializer
    )
from rezume.management.commands.parsedoc import DocRezume


class RezumeViewSet(ModelViewSet):
    queryset: QuerySet = Rezume.objects.all()
    permission_classes: tuple = (
            permissions.AllowAny,
        )        
    serializer_class = ResumeSerializer
    pagination_class = PageNumberPagination
    
    @action(
        methods=['post'],
        detail=False,
        url_path='pars',
        permission_classes=(
            permissions.AllowAny,
        ),
    )
    def parsedocresult(self, request: DRF_Request) -> DRF_Response:
        file_serializer = FileSerializer(data=request.data)
        print(FileSerializer(data=request.data))
        if file_serializer.is_valid():
            resume_data = DocRezume()
            resume_data.file = request.data['file']
            resume_data.handle()
            full_data_response: dict ={
                'full_name': resume_data.full_name,
                'email': resume_data.email,
                'phone_number': resume_data.phone,
                'education': resume_data.education,
                'experience': resume_data.experience,
                'skills': resume_data.skills
            }
            return DRF_Response(full_data_response)
        else:
            return DRF_Response(file_serializer.errors)    

    # def list(self, request: DRF_Request) -> DRF_Response:
        
    #     """Handles GET-request to show custom_users."""
    #     queryset: QuerySet = Rezume.objects.all()
    #     serializer: ResumeSerializer = ResumeSerializer( 
    #         self.queryset,
    #         many=True
    #         )
    #     return DRF_Response(
    #         serializer.data
    #     )

    # def create(self, request: DRF_Request, *args, **kwargs) -> DRF_Response:
    #     """Handles POST-request to show custom_users."""

    #     serializer: ResumeSerializer = ResumeSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()

    #         return DRF_Response(
    #             serializer.data
    #         )
    #     return DRF_Response(
    #         '???????????? ???? ????????????'
    #     )

    # def destroy(self, request, *args, **kwargs):
    #     return super().destroy(request, *args, **kwargs)

    # def partial_update(self, request, *args, **kwargs):
    #     return super().partial_update(request, *args, **kwargs)
