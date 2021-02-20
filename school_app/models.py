from django.db import models

class Person(models.Model):
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)

class Professor(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    salary = models.DecimalField(max_digits=8, decimal_places=2)
