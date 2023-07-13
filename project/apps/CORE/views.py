from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from .forms import AseguradoForm, AseguradoraForm, PolizaForm
from .models import Asegurado, Aseguradora, Poliza

def home(request):
    asegurados_registros = Asegurado.objects.all()
    return render(request, "CORE/index.html")

def index(requiest):
    return render(requiest, "CORE/index.html")


# Crear asegurados
def crear_asegurado(request: HttpRequest) -> HttpResponse:
     
    if request.method == "POST":
        form1 = AseguradoForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect("asegurado:home")
    
    else:  # request.method == "GET"
        form1 = AseguradoForm()
        return render(request, "CORE/crear.html", {"form": form1})



# Crear aseguradoras
def crear_aseguradora(request: HttpRequest) -> HttpResponse:
     
    if request.method == "POST":
        form2 = AseguradoraForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect("asegurado:home")
    
    else:  # request.method == "GET"
        form2 = AseguradoraForm()
        return render(request, "CORE/crear_aseguradora.html", {"form": form2})