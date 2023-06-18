from django.contrib import admin
from django.urls import path
from students_api.views import *

app_name = 'students_api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-retrieve-update-destroy'),
]