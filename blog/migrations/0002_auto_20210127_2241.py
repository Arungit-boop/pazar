# Generated by Django 3.0.11 on 2021-01-27 17:11

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(upload_to=blog.models.blog_thumbnail_directory_path),
        ),
    ]
