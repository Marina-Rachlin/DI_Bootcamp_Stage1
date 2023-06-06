from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.models import User


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        # Fetch the user with authenticate()
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user is not None:
            # Sign the user in using login()
            login(self.request, authenticated_user)
        return response
    

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home') 


def logout_view(request):
    logout(request)
    return redirect('home')


def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'profile.html', {'user': user})

