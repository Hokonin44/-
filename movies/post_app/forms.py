from django import forms
from post_app.models import Movie


class CreateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = 'title descriptions tags'.split()

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": 'form-control',
                    'placeholder': 'Enter a news title'

                }
            ),
            'descriptions': forms.Textarea(
                attrs={
                    "class": 'form-control',
                    'placeholder': 'Enter a news text'
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control-custom',
                    'placeholder': ''
                }
            )

        }