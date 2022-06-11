from rest_framework.serializers import ModelSerializer
from rezume.models import (
  Resume,
  )

class ResumeSerializer(ModelSerializer):
  class Meta():
    model = Resume
    fields =(
            'full_name',
            'email',
            'phone_number',
            'education',
            'experience',
            'skills'
            )


class FileSerializer(ModelSerializer):
  class Meta():
    model = Resume
    fields = (
      'file',
    )