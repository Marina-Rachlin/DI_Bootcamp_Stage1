from django import forms
from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField

class PhoneForm(forms.Form):
    # number = PhoneNumberField(region="IL")
    number = PhoneNumberField()