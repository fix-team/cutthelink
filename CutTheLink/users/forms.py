from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_slug


class UserRegistraionForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Email',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}),
        validators=[validate_slug]
    )
    password1 = forms.CharField(
        label='Введите пароль',
        help_text='Пароль не должен быть маленьким и простым',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistraionForm, self).__init__(*args, **kwargs)
        del self.fields['password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Введите Email',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}),
        validators=[validate_slug]
    )

    class Meta:
        model = User
        fields = ['username', 'email']
