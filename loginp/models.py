from django.db import models


class Register(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    

    