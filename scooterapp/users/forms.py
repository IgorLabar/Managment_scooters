from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


# Создал форму для регистрации
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Имя Пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        label="Имя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label="Пароль",  widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label="Подтвердите пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        label="Почта",  widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password1', 'password2', 'city', 'img')


# Форма для зарегистрировавшегося пользователя
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Имя Пользователя",  widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label="Пароль",  widget=forms.PasswordInput(attrs={'class': 'form-control'}))