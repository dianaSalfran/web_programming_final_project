from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Artista, Obra, Evento_resultado, Modalidad


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = '__all__'


class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = '__all__'


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento_resultado
        fields = '__all__'


class ModalidadForm(forms.ModelForm):
    class Meta:
        model = Modalidad
        fields = '__all__'
