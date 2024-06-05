from django import forms

from .models import Linia, Rola, Bohater

class LiniaForm(forms.ModelForm):
    class Meta:
        model = Linia
        fields = '__all__'


class RolaForm(forms.ModelForm):
    class Meta:
        model = Rola
        fields = '__all__'


class BohaterForm(forms.ModelForm):
    class Meta:
        model = Bohater
        fields = '__all__'