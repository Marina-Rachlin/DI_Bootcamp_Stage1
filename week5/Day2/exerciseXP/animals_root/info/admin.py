from django.contrib import admin
from .models import Family, Animal #import the Person model

# Register your models here.
admin.site.register(Animal)
admin.site.register(Family)
