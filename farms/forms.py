# forms.py
from django import forms
from .models import Farm

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['name', 'size_hectares', 'slug', 'farm_lat', 'farm_long']

    # better styled, but needs to be chnged to match model
    # farm_name = forms.CharField(label='Name', max_length=100,
    #     widget=forms.TextInput(attrs={'class': 'farm_name'}))
    # farm_size = forms.DecimalField(label='Size (hectares)', min_value=0, 
    #     widget=forms.TextInput(attrs={'class': 'farm_size'}))
    # farm_lat = forms.CharField(label='Latitude',
    #     widget=forms.TextInput(attrs={'class': 'farm_lat', 'placeholder': 'latitude'}))
    # farm_long = forms.CharField(label='Longitude',
    #     widget=forms.TextInput(attrs={'class': 'farm_long', 'placeholder': 'longitude'}))