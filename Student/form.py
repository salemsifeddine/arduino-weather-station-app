from .models import *
from django import forms

class WeatherForm(forms.ModelForm):
    class Meta:
        model = Weather
        fields = "__all__"
