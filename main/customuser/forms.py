from django import forms

class SignInForm(forms.Form):
    username = forms.CharField (
        max_length=200,
        required=True,
        label=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': 'Username',
        })
    )

    email = forms.EmailField(
        label=False,
        required=True,
        widget= forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'E-mail',
        })
    )

    password = forms.CharField(
        max_length=200,
        required=True,
        label=False,
        widget= forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        )
    )

class LogInForm(forms.Form):
    username = forms.CharField (
        max_length=200,
        required=True,
        label=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': 'Username',
        })
    )

    email = forms.EmailField(
        label=False,
        required=True,
        widget= forms.EmailInput(attrs={
            'class': 'form-control',
            'type': 'email',
            'placeholder': 'E-mail',
        })
    )
        
    password = forms.CharField(
        max_length=200,
        required=True,
        label=False,
        widget= forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        )
    )