from django.urls import path
from .views import crear_asegurado, home


app_name = "asegurado"

urlpatterns = [
    path("", home, name="home"),
        path('crear/', crear_asegurado, name="crear"),
   

]