# Generated by Django 3.0.11 on 2021-02-05 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pazar', '0010_auto_20210205_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='color',
            field=models.CharField(default='#D495B1', max_length=7),
        ),
    ]
