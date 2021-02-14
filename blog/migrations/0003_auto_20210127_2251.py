# Generated by Django 3.0.11 on 2021-01-27 17:21

import blog.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210127_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(upload_to=blog.models.blog_thumbnail_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]
