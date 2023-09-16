from django import forms
from .models import Links
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


# def validate_url(url):
#     validate = URLValidator(verify_exists=True)
#     try:
#         validate(url)
#     except ValidationError as e:
#         return False
#     return True


class AddLinkForm(forms.ModelForm):
    title = forms.CharField(
        label='Введите название ссылки',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название ссылки'})
    )
    short = forms.SlugField(
        label='Введите какую хотите короткую ссылку',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылка'}),
    )
    long = forms.URLField(
        label='Введите полную ссылку',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ссылка'})
    )

    class Meta:
        model = Links
        fields = ['title', 'short', 'long', 'user']
        widgets = {'user': forms.HiddenInput()}
