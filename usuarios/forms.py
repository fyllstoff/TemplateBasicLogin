from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class RegistroForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Contraseña",
        min_length=8
    )
    confirmar_password = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirmar Contraseña"
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.search(r'[A-Z]', password):
            raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r'[0-9]', password):
            raise ValidationError("La contraseña debe contener al menos un número.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmar_password = cleaned_data.get('confirmar_password')
        if password and confirmar_password and password != confirmar_password:
            raise ValidationError("Las contraseñas no coinciden.")
