# Generated by Django 4.2.6 on 2024-02-18 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0004_alter_modelunits_bresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelunits',
            name='bcontent',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='modelunits',
            name='bresponse',
            field=models.TextField(blank=True, default=''),
        ),
    ]
