from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey('Person',on_delete=models.CASCADE), 
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category')

class Category(models.Model):
    name = models.CharField(max_length=20)


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Email(models.Model):
    email = models.CharField(max_length=100)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True) 

    def __str__(self):
        return self.email
    
class Address(models.Model):
    location = models.CharField(max_length=100)
    people = models.ManyToManyField(Person, related_name='addresses') 

    def __str__(self):
        return self.location    


    
   

