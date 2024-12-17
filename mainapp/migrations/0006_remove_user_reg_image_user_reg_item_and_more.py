# Generated by Django 5.1 on 2024-12-17 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_user_reg_delete_userreg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_reg',
            name='Image',
        ),
        migrations.AddField(
            model_name='user_reg',
            name='Item',
            field=models.ImageField(null=True, upload_to='userimages'),
        ),
        migrations.AlterField(
            model_name='search',
            name='Item',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
