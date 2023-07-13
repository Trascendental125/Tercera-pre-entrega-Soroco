from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from CORE.forms import PolizaForm
from CORE.models import Poliza

def home(request):
    aseguradoras_registros = Poliza.objects.all()
    return render(request, "polizas/index.html")

def index(requiest):
    return render(requiest, "polizas/index.html")


# Crear poliza
def crear_poliza(request: HttpRequest) -> HttpResponse:
     
    if request.method == "POST":
        form = PolizaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("aseguradoras:home")
    
    else:  # request.method == "GET"
        form = PolizaForm()
        return render(request, "polizas/crear_poliza.html", {"form": form})
