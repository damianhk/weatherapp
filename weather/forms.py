from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'City name', 'aria-label': 'City name',
                                          'aria-describedby': 'basic-addon2', 'id': "1"})}
 