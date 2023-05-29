from django.urls import path
from .views import people_list, person

urlpatterns = [
    path('', people_list),
    path('<int:id>', person),
]
