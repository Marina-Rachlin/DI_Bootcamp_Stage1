from django.db import models

# Create your models here.

class Post(models.Model):
    
    title= models.CharField(max_length=50)
    content = models.TextField()
    author= models.CharField(max_length=20)
    dete_created= models. DateTimeField(auto_now_add=True)

