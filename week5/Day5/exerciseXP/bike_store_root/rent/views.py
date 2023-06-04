from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import CustomerForm, VehicleForm, RentalForm
from rent.models import Rental, Customer, Vehicle
from django.db.models import F



def home(request):
    return render(request, 'home.html',{})


class RentalHomeListView(ListView):
    model = Rental
    # template_name = 'rental_list.html'
    template_name = 'home.html'
    context_object_name = 'rentals'
    queryset = Rental.objects.order_by(F('return_date').asc(nulls_first=True), 'rental_date')

class RentalListView(ListView):
    model = Rental
    template_name = 'rental_list.html'
    context_object_name = 'rentals'
    queryset = Rental.objects.order_by(F('return_date').asc(nulls_first=True), 'rental_date')


class RentalDetailView(DetailView):
    model = Rental
    template_name = 'rental_detail.html'
    context_object_name = 'rental'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rental = self.get_object()
        context['customer'] = rental.customer
        context['vehicle'] = rental.vehicle
        return context


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    context_object_name = 'vehicle'  


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'
    queryset = Customer.objects.order_by('first_name', 'last_name')


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'
    queryset = Vehicle.objects.order_by()    


class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'
    context_object_name = 'vehicles'
    queryset = Vehicle.objects.order_by('vehicle_type') 


def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')  
    else:
        form = VehicleForm()
    return render(request, 'add_vehicle.html', {'form': form})


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})


def add_rental(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rental_list')  
    else:
        form = RentalForm()
    return render(request, 'add_rental.html', {'form': form})


