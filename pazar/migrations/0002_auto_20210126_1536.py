# Generated by Django 3.0.11 on 2021-01-26 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pazar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salebill',
            name='shop',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pazar.Free_Listing'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='color',
            field=models.CharField(default='#38AD2B', max_length=7),
        ),
    ]