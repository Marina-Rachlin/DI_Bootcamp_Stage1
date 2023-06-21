from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.core import serializers
import json


def homepage(request):
    return render(request, 'test.html')

def rooms_page(request):
    return render(request, 'room.html')


def category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {'category': category}
    return render(request, 'category_details.html', context)# fix the names

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('visitors:homepage')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        # Fetch the user with authenticate()
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user is not None:
            # Sign the user in using login()
            login(self.request, authenticated_user)
        return response
    

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('visitors:homepage') 
    

def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'visitors:homepage', {'user': user})    


def logout_view(request):
    logout(request)
    return redirect('visitors:homepage')


def booking_page(request):
    form = CheckAvailabilityForm()

    if request.method == 'POST':
        form = CheckAvailabilityForm(request.POST)
        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            num_guests = form.cleaned_data['num_guests']

            # Call the get_vacancies function and store the returned values in variables
            available_rooms = get_vacancies(check_in_date, check_out_date, num_guests)
            context = {'available_rooms': available_rooms}
            return redirect('visitors:vacancies', **context)
        
    context = {'form': form}
    return render(request, 'booking.html', context)


def get_vacancies(check_in_date, check_out_date, num_guests):
    """
    Get a list of available room options for the given date range and number of guests.
    Returns one room option per room type.
    """
    conflicting_bookings = Booking.objects.filter(
        Q(check_in_date__lt=check_out_date) & Q(check_out_date__gt=check_in_date) & Q(num_guests__gte=num_guests)
    )

    booked_rooms = [booking.room for booking in conflicting_bookings]
    all_rooms = Room.objects.all()
    available_rooms = []

    room_types = set(room.category for room in all_rooms)

    for room_type in room_types:
        room_options = [room for room in all_rooms if room.category == room_type and room not in booked_rooms]
        if room_options:
            available_rooms.append(room_options[0].category)  # Append the first room option of the room type

    # print(available_rooms)
    return available_rooms

def vacancies_view(request, available_rooms):
    context = {'available_rooms': available_rooms}
    return render(request, 'vacancies.html', context)



# def check_availability(request): # function handles the request to check the availability of a specific room
#     # Retrieve info from the request
#     check_in_date = request.POST.get('check_in_date')
#     check_out_date = request.POST.get('check_out_date')
#     num_guests = request.POST.get('num_guests') 

#     # Retrieve the room for which availability needs to be checked (e.g., based on room number or ID)
#     room_number = request.POST.get('room_number')
#     room = Room.objects.get(number=room_number)

#     # Check availability using the is_available method of the Booking model
#     is_available = room.is_available(check_in_date, check_out_date, num_guests)

#     # Render a response based on the availability status
#     return render(request, 'availability.html', {'is_available': is_available})


# def book_room(request, room_id):
#     room = Room.objects.get(id=room_id)

#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.room = room
#             booking.user = request.user  # Assuming you have user authentication
#             booking.save()
#             return redirect('booking_success')
#     else:
#         form = BookingForm()

#     return render(request, 'book_room.html', {'form': form, 'room': room})



# def write_review(request, room_id):
#     room = get_object_or_404(Room, id=room_id)

#     booking = Booking.objects.filter(user=request.user, room=room).first()
#     if not booking:
#         # Redirect or show an error message indicating that only guests who have booked the room can write a review
#         return HttpResponse("Only guests who have booked this room can write a review.")

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.user = request.user
#             review.room = room
#             review.save()
#             return redirect('room_detail', room_id=room.id)
#     else:
#         form = ReviewForm()

#     context = {
#         'room': room,
#         'booking': booking,
#         'form': form
#     }

#     return render(request, 'write_review.html', context)



