# Generated by Django 3.0.11 on 2021-02-07 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pazar', '0015_auto_20210207_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='color',
            field=models.CharField(default='#EEDF85', max_length=7),
        ),
    ]
