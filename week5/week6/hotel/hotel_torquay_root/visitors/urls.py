from django.contrib import admin
from django.urls import path
from .views import home
from django. conf. urls.static import static
from django.conf import settings

urlpatterns = [
   path('', home, name="home"),
]