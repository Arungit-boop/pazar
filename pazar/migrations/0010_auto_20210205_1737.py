# Generated by Django 3.0.11 on 2021-02-05 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pazar', '0009_auto_20210205_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='color',
            field=models.CharField(default='#2C6257', max_length=7),
        ),
    ]
