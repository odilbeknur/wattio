from django import forms
from .models import Inverter, Plant

class InverterForm(forms.ModelForm):
    class Meta:
        model = Inverter
        fields = ['name', 'serial', 'plant', 'color']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'serial': forms.TextInput(attrs={'class': 'form-control'}),
            'plant': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'color'
            }),
        }

    def __init__(self, *args, **kwargs):
        serial_choices = kwargs.pop('serial_choices', [])
        super(InverterForm, self).__init__(*args, **kwargs)
        self.fields['serial'].choices = serial_choices


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }