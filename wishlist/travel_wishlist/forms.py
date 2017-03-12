from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name',)


class NewInformationForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('date', 'notes',)
