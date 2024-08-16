from django import forms
from .models import Customuser

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Customuser
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'placeholder': 'E-mail',
                'autocomplete': 'off',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }),
        }



class LogInForm(forms.ModelForm):
    class Meta:
        model = Customuser
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'placeholder': 'E-mail',
                'autocomplete': 'off',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }),
        }
