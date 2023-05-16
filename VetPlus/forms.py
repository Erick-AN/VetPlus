from django import forms

from .models import InicioSesion,Busqueda_Cliente

class FormInicioSesion(forms.ModelForm):
    contrasenia = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = InicioSesion
        fields = '__all__'

class FormBusqueda_Cliente(forms.ModelForm):
    class Meta:
        model = Busqueda_Cliente
        fields = '__all__'