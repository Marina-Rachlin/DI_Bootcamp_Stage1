from django import forms
from django.forms import formset_factory
from .models import *


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__' 

class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = '__all__'      


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['review_text'].widget = forms.Textarea(attrs={'rows': 3})
        self.fields['rating'].widget = forms.RadioSelect(choices=[(i, i) for i in range(1, 6)])


class AddPosterForm(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ['image', 'explanation_img']


class AddFilmWithPosterForm(forms.ModelForm):
    poster_image = forms.ImageField(required=True, label='Poster Image')
    poster_explanation_img = forms.CharField(max_length=255, required=True, label='Poster Explanation')

    class Meta:
        model = Film
        fields = ['title', 'release_date', 'created_in_country', 'available_in_countries', 'category', 'director']

    def save(self, commit=True):
        film = super().save(commit=False)
        if commit:
            film.save()
        poster = Poster(film=film, image=self.cleaned_data['poster_image'], explanation_img=self.cleaned_data['poster_explanation_img'])
        poster.save()
        return film

ProducerFormSet = forms.modelformset_factory(model=Producer, form=ProducerForm)