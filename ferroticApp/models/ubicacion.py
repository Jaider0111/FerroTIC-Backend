from django.db import models


class Ubicacion(models.Model):
    idUbicacion = models.BigAutoField(primary_key=True)
    departamento = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    direccion = models.CharField(max_length=60)
    barrio = models.CharField(max_length=60, null=True)
    numeroInmueble = models.IntegerField(null=True)
    instruccionesAdicionales = models.TextField(null=True)
    estado = models.CharField(max_length=60)
    fechaActualizacion = models.DateTimeField(null=True)
