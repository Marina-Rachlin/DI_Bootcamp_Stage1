from django import forms
from .models import Gif, Category

class GifForm(forms.ModelForm):
    class Meta:
        model = Gif
        fields ='__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields ='__all__'        

