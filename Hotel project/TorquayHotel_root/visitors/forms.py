from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
from .models import *


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

class LoginForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'
        

class CheckAvailabilityForm(forms.Form):
    check_in_date = forms.DateField()
    check_out_date = forms.DateField()
    num_guests = forms.IntegerField()   


class GuestDetailsForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=20)
    additional_details = forms.CharField(widget=forms.Textarea)
    preferences = forms.CharField(widget=forms.Textarea)     


# class BookingForm(forms.Form):
#     check_in_date = forms.DateField(label='Check-in Date')
#     check_out_date = forms.DateField(label='Check-out Date')
#     num_adults = forms.IntegerField(label='Number of Adults')
#     num_children = forms.IntegerField(label='Number of Children')
#     promotional_code = forms.CharField(label='Promotional Code', required=False)
#     guest_name = forms.CharField(max_length=100)
#     guest_email = forms.EmailField()
#     guest_phone = forms.CharField(max_length=20)
#     special_requests = forms.CharField(widget=forms.Textarea, required=False)
#     payment_method = forms.ChoiceField(choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')])

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = '__all__'
        

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['rating', 'comment']




