from email import message
from django.db import models
# Create your models here.


class contact(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    password=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)
    gender=models.CharField(max_length=30)

class contactus(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.TextField(max_length=600)

class subscribe(models.Model):
    email=models.EmailField(max_length=50)