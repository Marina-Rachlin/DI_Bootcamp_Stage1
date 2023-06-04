"""
URL configuration for bike_store project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rent.views import RentalListView, RentalDetailView, CustomerDetailView, CustomerListView, VehicleListView, VehicleDetailView,add_customer, add_rental, add_vehicle, RentalHomeListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RentalHomeListView.as_view(), name='home'),
    path('rental/list', RentalListView.as_view(), name='rental_list'),
    path('rental/<int:pk>/', RentalDetailView.as_view(), name='rental_detail'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/', CustomerListView.as_view(), name='customer_list'),
    path('vehicle/', VehicleListView.as_view(), name='vehicle_list'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle_detail'),
    path('customer/add/', add_customer, name='add_customer'),
    path('vehicle/add/', add_vehicle, name='add_vehicle'),
    path('rental/add/', add_rental, name='add_rental'),
]


