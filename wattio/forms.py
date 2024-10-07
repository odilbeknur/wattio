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
        fields = [
            'name', 'power', 'country', 'city', 
            'address', 'timezone', 'longitude', 
            'latitude', 'image'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название станции'
            }),
            'power': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Общая мощность (кВт)'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Страна'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес'
            }),
            'timezone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Часовой пояс'
            }),
            'longitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Долгота'
            }),
            'latitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Широта'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',  # For file inputs
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('Название станции обязательно.')
        return name

    def clean_power(self):
        power = self.cleaned_data.get('power')
        if power is None:
            raise forms.ValidationError('Общая мощность обязательна.')
        if power < 0:
            raise forms.ValidationError('Общая мощность должна быть положительным числом.')
        return power

    # def clean_longitude(self):
    #     longitude = self.cleaned_data.get('longitude')
    #     if longitude is None:
    #         raise forms.ValidationError('Долгота обязательна.')
    #     if longitude < -180 or longitude > 180:
    #         raise forms.ValidationError('Долгота должна быть в диапазоне от -180 до 180.')
    #     return longitude

    # def clean_latitude(self):
    #     latitude = self.cleaned_data.get('latitude')
    #     if latitude is None:
    #         raise forms.ValidationError('Широта обязательна.')
    #     if latitude < -90 or latitude > 90:
    #         raise forms.ValidationError('Широта должна быть в диапазоне от -90 до 90.')
    #     return latitude

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Check for valid image file type (e.g., jpg, png)
            valid_extensions = ['.jpg', '.jpeg', '.png']
            if not any(image.name.endswith(ext) for ext in valid_extensions):
                raise forms.ValidationError('Поддерживаемые форматы: jpg, jpeg, png.')
        return image
