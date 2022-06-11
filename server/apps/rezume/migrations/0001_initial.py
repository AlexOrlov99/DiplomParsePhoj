# Generated by Django 4.0.4 on 2022-05-19 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now=True, verbose_name='время создания')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаления')),
                ('title', models.CharField(max_length=50, verbose_name='Название файла')),
                ('obj', models.FileField(max_length=255, upload_to='rezume_files/%Y/%m/%d', verbose_name='Объект документа')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
                'ordering': ('-datetime_created',),
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now=True, verbose_name='время создания')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаления')),
                ('full_name', models.CharField(max_length=50, verbose_name='Полное имя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта/Логин')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('education', models.TextField(default='', verbose_name='Образование')),
                ('skills', models.TextField(default='', verbose_name='Проффесиональные навыки')),
                ('experience', models.TextField(default='', verbose_name='Проффесиональные навыки')),
                ('file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rezume.file', verbose_name='вложенный файл')),
            ],
            options={
                'verbose_name': 'Резюме',
                'verbose_name_plural': 'Резюме',
                'ordering': ('-datetime_created',),
            },
        ),
    ]
