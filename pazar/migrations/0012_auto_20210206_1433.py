# Generated by Django 3.0.11 on 2021-02-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pazar', '0011_auto_20210205_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='color',
            field=models.CharField(default='#73B607', max_length=7),
        ),
    ]
