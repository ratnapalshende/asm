from django import forms
from .models import UserRegistration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Use PasswordInput widget for password field
        }
