from django.db import models

class Person(models.Model):
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
