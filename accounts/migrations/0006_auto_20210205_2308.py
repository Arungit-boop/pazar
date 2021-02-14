# Generated by Django 3.0.11 on 2021-02-05 17:38

import accounts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210205_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfilecontent',
            name='file',
            field=models.ImageField(upload_to=accounts.models.post_images_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]
