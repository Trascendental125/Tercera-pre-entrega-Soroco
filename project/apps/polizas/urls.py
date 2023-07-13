from django.urls import path
from .views import home, crear_poliza


app_name = "polizas"

urlpatterns = [
    path("", home, name="home"),
    path('crear_poliza/', crear_poliza, name="crear_poliza"),

]