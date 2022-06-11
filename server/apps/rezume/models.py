from datetime import datetime

from django.db.models import (
    Model,
    QuerySet,
    ManyToManyField,
    ForeignKey,
    OneToOneField,
    CharField,
    TextField,
    IntegerField,
    DateTimeField,
    FileField,
    EmailField,
    DateField,
    ImageField,
    PROTECT,
    CASCADE,
)
from abstracts.models import AbstractDateTime
from auths.models import CustomUser


class ResumeQuerySet(QuerySet):

    def get_not_deleted(self) -> QuerySet:
        return self.filter(
            datetime_deleted__isnull=True
        )


class Resume(AbstractDateTime):

    FILE_TYPE = 'docx'

    file = FileField(
        verbose_name='Объект документа',
        upload_to='rezume_files/%Y/%m/%d',
        max_length=255
    )
    
    full_name = CharField(
        max_length=50,
        verbose_name='Полное имя',
    )
    email = EmailField(
        verbose_name='Почта/Логин', 
        unique=True,
    )
    phone_number = CharField(
        max_length=20,
        verbose_name='Номер телефона',
        null=True,
        blank=True,
    )
    education = TextField(
        verbose_name='Образование',
        default='',       
    )
    experience = TextField(
        verbose_name='Опыт работы',
        default='',
    )
    skills = TextField(
        verbose_name='Проффесиональные навыки',
        default='',
    )
  
    objects = ResumeQuerySet().as_manager()

    def __str__(self) -> str:
        return f'{self.full_name} | {self.email}'

    class Meta:
        ordering = (
            '-datetime_created',
        )
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'