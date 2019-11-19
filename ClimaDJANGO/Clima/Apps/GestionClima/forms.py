from django.forms import ModelForm
from django import forms


from .models import *


class ContactForm(ModelForm):
    Nombre = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    Email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))
    Messg = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ), label='Mensaje')

    class Meta:
        model = Contactanos
        fields = ['Nombre', 'Email', 'Messg']


class RegisterForm(ModelForm):
    Nombre = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    Email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))
    Pass1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ), label='Contraseña')

    Pass2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ), label='Confirmar Contraseña')

    Fono = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), label='Teléfono')
    #campo extra para imagen
    Imagen = forms.ImageField(widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        ), label='Imagen')

    class Meta:
        model = Cuenta
        fields = ['Nombre', 'Email', 'Pass1', 'Pass2', 'Fono', 'Imagen']


class TipoUserForm(ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    tipo = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = TipoUser
        fields = ['nombre', 'tipo']