# Generated by Django 5.1 on 2024-12-17 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_user_reg_image_user_reg_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_reg',
            name='Item',
        ),
        migrations.AddField(
            model_name='user_reg',
            name='Image',
            field=models.ImageField(null=True, upload_to='userimages'),
        ),
    ]
