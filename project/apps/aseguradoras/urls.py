from django.urls import path
from .views import crear_aseguradora, home


app_name = "aseguradoras"

urlpatterns = [
    path("", home , name="home"),
    path('crear_aseguradora/', crear_aseguradora, name="crear_aseguradora"),

]


