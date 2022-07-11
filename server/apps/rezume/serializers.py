from rest_framework.serializers import ModelSerializer
from rezume.models import (
  Rezume,
  )

class ResumeSerializer(ModelSerializer):
  class Meta():
    model = Rezume
    fields =(
            'id',
            'full_name',
            'email',
            'phone_number',
            'education',
            'experience',
            'skills'
            )


class FileSerializer(ModelSerializer):
  class Meta():
    model = Rezume
    fields = (
      'file',
    )