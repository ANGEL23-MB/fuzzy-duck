# Generated by Django 5.1 on 2024-12-17 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sever_reg',
            name='sPh',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sever_reg',
            name='syear',
            field=models.IntegerField(),
        ),
    ]
