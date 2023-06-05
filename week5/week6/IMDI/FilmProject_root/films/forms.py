from django import forms
from .models import Director, Film, Review


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'       


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['review_text'].widget = forms.Textarea(attrs={'rows': 3})
        self.fields['rating'].widget = forms.RadioSelect(choices=[(i, i) for i in range(1, 6)])
        