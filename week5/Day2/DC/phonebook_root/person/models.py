from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = PhoneNumberField(region='IL')
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name