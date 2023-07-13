from django.db import models

# Create your models here.
class Asegurado(models.Model):
    nombre = models.CharField(max_length=100)
    cuit = models.IntegerField()
    # Otros campos necesarios para el asegurado
    def __str__(self):
        return self.nombre


class Aseguradora(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    # Otros campos necesarios para la aseguradora

    def __str__(self):
        return self.nombre


class Poliza(models.Model):
    asegurado = models.ForeignKey(Asegurado, on_delete=models.SET_NULL, null=True, blank=True)
    aseguradora = models.ForeignKey(Aseguradora, on_delete=models.SET_NULL, null=True, blank=True)
    seccion = models.CharField(max_length=100, blank=True)
    numero_poliza = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.numero_poliza