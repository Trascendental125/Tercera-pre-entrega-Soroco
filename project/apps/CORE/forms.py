from django import forms

from .models import Asegurado, Aseguradora, Poliza

class AseguradoForm(forms.ModelForm):
    class Meta:
        model = Asegurado
        fields = ['nombre', 'cuit']

class AseguradoraForm(forms.ModelForm):
    class Meta:
        model = Aseguradora
        fields = ['nombre', 'pais',]

class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = ['asegurado', 'aseguradora', 'seccion', 'numero_poliza']


 
