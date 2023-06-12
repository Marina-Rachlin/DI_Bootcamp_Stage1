from pyexpat.errors import messages
from django.views.generic import ListView
from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy

#home_page
def home(request):
    context = {
        'page_title': "Torquay Hotel",
    }
    return render(request, 'index.html', context)