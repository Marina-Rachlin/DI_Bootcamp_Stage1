from django.shortcuts import render
from .models import *

# Create your views here.

def profile(request):
    current_user = Person.objects.get(first_name='John')
    addresses = current_user.addresses.all()

    user_email = current_user.email

    context ={'user': current_user, 'email': user_email, 'addresses': addresses}

    return render(request, 'profile.html',context)
