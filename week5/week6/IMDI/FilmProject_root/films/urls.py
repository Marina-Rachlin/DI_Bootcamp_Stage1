from django.contrib import admin
from django.urls import path
from .views import HomePageView, FilmCreateView, DirectorCreateView, ReviewCreateView

urlpatterns = [
    path('homepage', HomePageView.as_view(), name='home'),
    path('addFilm/', FilmCreateView.as_view(), name = 'addFilm'),
    path('addDirector/',DirectorCreateView.as_view(), name = 'addDirector'),
    path('addReview//<int:film_id>/',ReviewCreateView.as_view(), name = 'addReview')
]