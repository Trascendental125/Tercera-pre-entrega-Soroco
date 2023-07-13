from django.urls import path
from .views import home, crear_asegurado


app_name = "asegurado"

urlpatterns = [
    path("", home, name="home"),
    path('crear/', crear_asegurado, name="crear"),


]