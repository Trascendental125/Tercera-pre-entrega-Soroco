from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from CORE.forms import AseguradoraForm
from CORE.models import Aseguradora

def home(request):
    aseguradoras_registros = Aseguradora.objects.all()
    return render(request, "aseguradoras/index.html")

def index(requiest):
    return render(requiest, "aseguradoras/index.html")


# Crear asegurados
def crear_aseguradora(request: HttpRequest) -> HttpResponse:
     
    if request.method == "POST":
        form = AseguradoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("aseguradoras:home")
    
    else:  # request.method == "GET"
        form = AseguradoraForm()
        return render(request, "aseguradoras/crear_aseguradora.html", {"form": form})
