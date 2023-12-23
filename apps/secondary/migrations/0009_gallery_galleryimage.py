# Generated by Django 5.0 on 2023-12-22 09:11

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0008_remove_place_descriptions_placeinlineinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галерея',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery', verbose_name='Фотография')),
                ('place_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_image', to='secondary.gallery')),
            ],
            options={
                'unique_together': {('place_info', 'image')},
            },
        ),
    ]