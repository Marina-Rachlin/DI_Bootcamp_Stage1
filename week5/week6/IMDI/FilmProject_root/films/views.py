from django.views.generic import ListView, CreateView
from django.shortcuts import render
from .models import *
from .forms import FilmForm, DirectorForm, ReviewForm
from django.urls import reverse_lazy


# Create your views here.
class HomePageView(ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'films'


class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'film/addFilm.html' 
    success_url = reverse_lazy('home')

class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm  
    template_name = 'director/addDirector.html'  
    success_url = reverse_lazy("home")# use the name of the path from urls


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/addReview.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.film_id = self.kwargs['film_id']
        return super().form_valid(form)