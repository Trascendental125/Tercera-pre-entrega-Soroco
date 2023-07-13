from django.urls import path
from .views import home, crear_asegurado, crear_aseguradora #crear_poliza


app_name = "asegurado"

urlpatterns = [
    path("", home, name="home"),
    path('crear/', crear_asegurado, name="crear"),
    path('crear_aseguradora/', crear_aseguradora, name="crear_aseguradora"),

]