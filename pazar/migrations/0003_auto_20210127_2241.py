# Generated by Django 3.0.11 on 2021-01-27 17:11

import django.core.validators
from django.db import migrations, models
import pazar.models


class Migration(migrations.Migration):

    dependencies = [
        ('pazar', '0002_auto_20210126_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise_with_us',
            name='Business_Images',
            field=models.ImageField(blank=True, null=True, upload_to=pazar.models.advertise_images_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], verbose_name='Business Images'),
        ),
        migrations.AlterField(
            model_name='advertise_with_us',
            name='Business_Logo',
            field=models.ImageField(upload_to=pazar.models.advertise_logo_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='advertisewithusimage',
            name='image',
            field=models.ImageField(upload_to=pazar.models.advertise_multiple_images_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='free_listing',
            name='Business_Images',
            field=models.ImageField(blank=True, null=True, upload_to=pazar.models.listing_images_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])], verbose_name='Business Images'),
        ),
        migrations.AlterField(
            model_name='free_listing',
            name='Business_Logo',
            field=models.ImageField(upload_to=pazar.models.listing_logo_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='freelistingimage',
            name='image',
            field=models.ImageField(upload_to=pazar.models.listing_multiple_images_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=pazar.models.product_images_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='skill',
            name='color',
            field=models.CharField(default='#FC98DF', max_length=7),
        ),
        migrations.AlterField(
            model_name='stock',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=pazar.models.stock_images_directory_path, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]