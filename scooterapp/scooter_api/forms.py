from django import forms
from users.models import CustomUser
from .models import Scooter, Trip


# Создал форму для того, чтобы пользователи могли изменять аватарку
class ImageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('img',)


# Форма создания самоката
class AddScooter(forms.ModelForm):
    serial_number = forms.CharField(max_length=6,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control'})
                                    )
    latitude = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    longitude = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    charge = forms.CharField(max_length=4,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control'})
                             )
    STATUS = (
        ('Free', 'Свободный'),
        ('Charge', 'Заряжается'),
        ('Repair', 'На ремонте'),
        ('Is used', 'Используется'),
    )
    active = forms.ChoiceField(choices=STATUS)

    class Meta:
        model = Scooter
        fields = ('__all__')


# Форма для бронирования самоката
class BookingScooter(forms.ModelForm):


    class Meta:
        model = Trip
        fields = ('scooter', 'cost', 'date_of_trip')
