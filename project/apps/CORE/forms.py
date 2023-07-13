from django import forms

from .models import Asegurado

class AseguradoForm(forms.ModelForm):
    class Meta:
        model = Asegurado
        fields = ['nombre', 'cuit']




 
