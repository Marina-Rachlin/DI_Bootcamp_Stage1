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
    num_adults = forms.IntegerField()
    num_kids = forms.IntegerField()   

    def __init__(self, *args, **kwargs):
        super(CheckAvailabilityForm, self).__init__(*args, **kwargs)
        num_kids = self.initial.get('num_kids', 0)
        for i in range(num_kids):
            field_name = f'child_age_{i+1}'
            label = f'Child {i+1} Age'
            self.fields[field_name] = forms.IntegerField(label=label)


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


# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ['rating', 'comment']




