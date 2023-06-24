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


class GuestDetailsForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = GuestDetails
        fields = ['first_name', 'last_name', 'phone', 'email', 'country', 'city', 'zip_code', 'additional_details']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(GuestDetailsForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

# class BookingGuestForm(forms.Form):
#     booking_form = BookingForm()
#     guest_details_form = GuestDetailsForm()

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




