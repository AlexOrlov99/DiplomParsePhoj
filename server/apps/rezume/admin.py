from django.contrib import admin

from rezume.models import (
    Resume,

)


class ResumeAdmin(admin.ModelAdmin):

    redonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )

admin.site.register(
    Resume, ResumeAdmin,
)
