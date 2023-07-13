from django.urls import path
from .views import home, crear_aseguradora


app_name = "aseguradoras"

urlpatterns = [
    path("", home, name="home"),
    path('crear_aseguradora/', crear_aseguradora, name="crear_aseguradora"),

]

from django.urls import path
from .views import home, crear_aseguradora

