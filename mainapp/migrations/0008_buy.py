# Generated by Django 5.1 on 2024-12-18 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_remove_user_reg_item_user_reg_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, null=True)),
                ('Item', models.CharField(max_length=200, null=True)),
                ('Description', models.CharField(max_length=9000, null=True)),
            ],
        ),
    ]