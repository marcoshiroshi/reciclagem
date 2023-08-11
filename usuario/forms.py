from django import forms
from django.contrib.auth.forms import UserChangeForm, BaseUserCreationForm
from .models import User


class SignUpForm(BaseUserCreationForm):

    class Meta:
        model = User
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@exemplo.com'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu email'}),
        }
        fields = ('email', 'first_name', 'last_name')


class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
