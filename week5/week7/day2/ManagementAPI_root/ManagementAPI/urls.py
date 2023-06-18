"""
URL configuration for ManagementAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from managementAPI_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include ("rest_framework.urls")),
    path('departments/', DepartmentListAPIView.as_view(), name='department-list'),
    path('departments/create/', DepartmentCreateAPIView.as_view(), name='department-create'),
    path('employees/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employees/create/', EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('projects/<int:id>/', ProjectRetrieveAPIView.as_view(), name='project-retrieve'),
    path('projects/<int:id>/update/', ProjectUpdateAPIView.as_view(), name='project-update'),
    path('projects/<int:id>/delete/', ProjectDestroyAPIView.as_view(), name='project-delete'),
    path('tasks/<int:id>/', TaskRetrieveAPIView.as_view(), name='task-retrieve'),
    path('tasks/<int:id>/update/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('tasks/<int:id>/delete/', TaskDestroyAPIView.as_view(), name='task-delete'),
]
