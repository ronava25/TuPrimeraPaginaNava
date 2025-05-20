from django import forms
from .models import Cliente, Servicio, Contratacion

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class ContratacionForm(forms.ModelForm):
    class Meta:
        model = Contratacion
        fields = '__all__'

class BusquedaClienteForm(forms.Form):
    nombre = forms.CharField(label="Buscar cliente por nombre")
