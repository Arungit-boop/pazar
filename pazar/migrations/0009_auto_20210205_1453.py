# Generated by Django 3.0.11 on 2021-02-05 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pazar', '0008_auto_20210205_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='color',
            field=models.CharField(default='#F78EFF', max_length=7),
        ),
    ]
