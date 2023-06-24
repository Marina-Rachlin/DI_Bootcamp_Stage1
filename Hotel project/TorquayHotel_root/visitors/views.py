from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from datetime import datetime
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import *
from .models import *


def homepage(request):
    return render(request, 'test.html')

def rooms_page(request):
    return render(request, 'room.html')

def booking_room_view(request):
    return render(request, 'room.html')

def category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {'category': category}
    return render(request, 'category_details.html', context)# fix the names

def check_availability(request):

    if request.method == 'POST':
        form = CheckAvailabilityForm(request.POST)
        if form.is_valid():
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            num_guests = form.cleaned_data['num_guests']

            # Call the get_vacancies function and store the returned values in variables
            available_rooms = get_vacancies(check_in_date, check_out_date, num_guests)
            context = {
                'available_rooms': available_rooms,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date,
                'num_guests': num_guests
                }
            
            return render(request, 'vacancies.html', context)

    form = CheckAvailabilityForm()   
    context = {'form': form}
    return render(request, 'booking.html', context)


def get_vacancies(check_in_date, check_out_date, num_guests):
    """
    Get a list of available room options for the given date range and number of guests (one option per room category).
    """
    conflicting_bookings = Booking.objects.filter(
        Q(check_in_date__lt=check_out_date) & Q(check_out_date__gt=check_in_date)
    )
    booked_rooms = [booking.room for booking in conflicting_bookings]
    room_types = Category.objects.filter(capacity__gte=num_guests)
    available_rooms = [room.category for room in Room.objects.all() if room.category in room_types and room not in booked_rooms]

    return available_rooms


def reservation(request):
    room_category = request.GET.get('room')
    category = get_object_or_404(Category, name=room_category)
    room = category
    check_in_date_str = request.GET.get('check_in_date')
    check_out_date_str = request.GET.get('check_out_date')
    num_guests = request.GET.get('num_guests')
    user = request.user

    if request.method == 'POST':
        guest_details_form = GuestDetailsForm(request.POST, user=user)
        if guest_details_form.is_valid():
            guest_details = guest_details_form.save(commit=False)
            guest_details.user = user
            guest_details.save()
            room = get_object_or_404(Room, category=room)

            # Create a booking object
            booking = Booking.objects.create(
                user=user,
                room=room,
                check_in_date = datetime.strptime(check_in_date_str, '%B %d, %Y').strftime('%Y-%m-%d'),
                check_out_date = datetime.strptime(check_out_date_str, '%B %d, %Y').strftime('%Y-%m-%d'),
                num_guests=num_guests,
                guest_details=guest_details
            )

            # Perform additional actions if needed

            return redirect('visitors:homepage')
    else:
        guest_details_form = GuestDetailsForm(user=user)

    context = {
        'room': room,
        'check_in_date': check_in_date_str,
        'check_out_date': check_out_date_str,
        'num_guests': num_guests,
        'user_name': user.first_name,
        'form': guest_details_form
    }

    return render(request, 'reservation.html', context)


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



