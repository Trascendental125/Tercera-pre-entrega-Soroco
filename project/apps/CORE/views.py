from django.shortcuts import render


from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from .forms import AseguradoForm

from .models import Asegurado

def home(request):
    asegurados_registros = Asegurado.objects.all()
    return render(request, "CORE/index.html")

def index(requiest):
    return render(requiest, "CORE/index.html")


# Crear asegurados
def crear_asegurado(request: HttpRequest) -> HttpResponse:
     
    if request.method == "POST":
        form = AseguradoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("asegurado:home")
    
    else:  # request.method == "GET"
        form = AseguradoForm()
        return render(request, "CORE/crear_aseguradora.html", {"form": form})



# Crear aseguradoras
def crear_aseguradora(request: HttpRequest) -> HttpResponse:
     
    if request.method == "POST":
        form = AseguradoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("asegurado:home")
    
    else:  # request.method == "GET"
        form = AseguradoraForm()
        return render(request, "CORE/crear_aseguradora.html", {"form": form})