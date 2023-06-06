from django.urls import path
from .views import *


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name = 'logout'),
    path('profile/<int:user_id>/', profile_view, name='profile'),
]