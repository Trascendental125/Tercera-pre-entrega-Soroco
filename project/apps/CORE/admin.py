from django.contrib import admin

# Register your models here.

from . import models 

admin.site.register(models.Asegurado)
admin.site.register(models.Aseguradora)
admin.site.register(models.Poliza)