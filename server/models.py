from django.db import models

# Create your models here.
class Sever_Reg(models.Model):
    sname = models.CharField(max_length=20)
    semail = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    sImage = models.ImageField(upload_to='serverimages')
    sloc = models.CharField(max_length=25)
    saddress = models.CharField(max_length=200)
    sPh = models.IntegerField()
    syear = models.IntegerField()
    