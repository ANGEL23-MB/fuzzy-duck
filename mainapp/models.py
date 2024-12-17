from django.db import models

# Create your models here.
#database table


# class userreg(models.Model):
#     Name = models.CharField(max_length=20)
#     Email = models.CharField(max_length=50)
#     Password = models.CharField(max_length=20)
#     Images = models.ImageField(upload_to='profile/',null=True)


class User_Reg(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    Image = models.ImageField(upload_to='userimages',null=True)


class search(models.Model):
    Item = models.CharField(max_length=200,null=True)
    Description = models.CharField(max_length=10000,null=True)
    Price = models.FloatField(null=True)


class Buy(models.Model):
    email = models.CharField(max_length=50, null=True)
    Item = models.CharField(max_length=200,null=True)
    Description = models.CharField(max_length=9000,null=True)

