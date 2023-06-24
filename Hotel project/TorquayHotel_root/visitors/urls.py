from django.urls import path
from . import views
from .views import *

app_name = 'visitors'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('rooms/', views.rooms_page, name='rooms_page'),
    path('booking/', views.check_availability, name='check_availability'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name = 'logout'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
    path('rooms/<int:category_id>/', views.category_view, name='category_view'),
    path('vacancies/', views.check_availability, name='vacancies'),
    path('rooms/', views.booking_room_view, name='booking_room_view'),
    path('reservation/', views.reservation, name='reservation_view'),
]


