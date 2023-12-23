# Generated by Django 5.0 on 2023-12-21 10:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_alter_projects_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kvartal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_europe', verbose_name='Фотография ')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст')),
            ],
            options={
                'verbose_name': 'Квартал',
                'verbose_name_plural': 'Кварталы',
            },
        ),
    ]