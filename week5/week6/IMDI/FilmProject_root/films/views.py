from pyexpat.errors import messages
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from .models import *
from .forms import FilmForm, DirectorForm, ReviewForm, AddFilmWithPosterForm
from django.urls import reverse_lazy


# Create your views here.
class HomePageView(ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'films'


class FilmCreateView(CreateView):
    model = Film
    # form_class = FilmForm
    form_class = AddFilmWithPosterForm
    template_name = 'film/addFilm.html' 
    success_url = reverse_lazy('home')
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poster'] = None  # Set default value for the poster

        # Retrieve the associated poster if it exists
        if self.object and hasattr(self.object, 'poster'):
            context['poster'] = self.object.poster

        return context


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
    


class FilmDeleteView(UserPassesTestMixin, DeleteView):
    model = Film
    template_name = 'film/confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Film deleted successfully.')
        return super().delete(request, *args, **kwargs)    