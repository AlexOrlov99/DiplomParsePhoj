# Generated by Django 4.0.5 on 2022-06-02 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezume', '0002_alter_resume_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='file',
            field=models.FileField(max_length=255, upload_to='rezume_files/%Y/%m/%d', verbose_name='Объект документа'),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]