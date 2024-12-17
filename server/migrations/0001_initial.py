# Generated by Django 5.1 on 2024-12-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sever_Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('semail', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('sImage', models.ImageField(upload_to='serverimages')),
                ('sloc', models.CharField(max_length=25)),
                ('saddress', models.CharField(max_length=200)),
                ('sPh', models.IntegerField(max_length=10)),
                ('syear', models.IntegerField(max_length=5)),
            ],
        ),
    ]