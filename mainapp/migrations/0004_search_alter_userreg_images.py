# Generated by Django 5.1 on 2024-11-29 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_userreg_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=25, null=True)),
                ('Price', models.FloatField(null=True)),
                ('Description', models.CharField(max_length=10000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='userreg',
            name='Images',
            field=models.ImageField(null=True, upload_to='profile/'),
        ),
    ]
