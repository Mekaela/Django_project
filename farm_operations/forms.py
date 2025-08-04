# forms.py
from django import forms
from .models import Fertilisation, Irrigation, Planting, Harvesting, PesticideApplication
# from crops.models import Crop

class OperationTypeForm(forms.Form):
    OPERATION_TYPE_CHOICES = [
        ('FERT', 'Fertilisation'),
        ('IRR', 'Irrigation'),
        ('PLANT', 'Planting'),
        ('HARV', 'Harvesting'),
        ('PEST', 'PesticideApplication'),
    ]
    operation_type = forms.ChoiceField(choices=OPERATION_TYPE_CHOICES, label='Record Type', required=True)

# class OpsForm(forms.ModelForm):
#     class Meta:
#         model = FarmOperation
#         fields = ['name', 'size_hectares', 'slug', 'farm_lat', 'farm_long']

    # better styled, but needs to be chnged to match model
    # farm_name = forms.CharField(label='Name', max_length=100,
    #     widget=forms.TextInput(attrs={'class': 'farm_name'}))
    # farm_size = forms.DecimalField(label='Size (hectares)', min_value=0, 
    #     widget=forms.TextInput(attrs={'class': 'farm_size'}))
    # farm_lat = forms.CharField(label='Latitude',
    #     widget=forms.TextInput(attrs={'class': 'farm_lat', 'placeholder': 'latitude'}))
    # farm_long = forms.CharField(label='Longitude',
    #     widget=forms.TextInput(attrs={'class': 'farm_long', 'placeholder': 'longitude'}))

class FertilisationForm(forms.ModelForm):
    fertilizer_type = forms.CharField(max_length=100, required=False)
    npk_ratio = forms.CharField(max_length=10, required=False)  # e.g., "10-20-10"
    application_method = forms.CharField(max_length=50, required=False)  # e.g., "Broadcast", "Banding", "Foliar-spray"
    application_rate = forms.FloatField(required=False)  # kg/ha
    class Meta:
        model = Fertilisation
        fields = '__all__'
        widgets = {
            'operation_type': forms.HiddenInput(),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
        required = False

class IrrigationForm(forms.ModelForm):
    class Meta:
        model = Irrigation
        fields = '__all__'
        widgets = {
            'operation_type': forms.HiddenInput(),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class PlantingForm(forms.ModelForm):
    class Meta:
        model = Planting
        fields = '__all__'
        widgets = {
            'operation_type': forms.HiddenInput(),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class HarvestingForm(forms.ModelForm):
    class Meta:
        model = Harvesting
        fields = '__all__'
        widgets = {
            'operation_type': forms.HiddenInput(),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class PesticideApplicationForm(forms.ModelForm):
    class Meta:
        model = PesticideApplication
        fields = '__all__'
        widgets = {
            'operation_type': forms.HiddenInput(),
            'date': forms.DateInput(attrs={'type': 'date'}),
        }