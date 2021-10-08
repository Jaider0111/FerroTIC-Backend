from django.db import models


class Ubicacion(models.Model):
    idUbicacion = models.BigAutoField(primary_key=True)
    departamento = models.IntegerField(default=0)
    ciudad = models.DateTimeField()
    direccion = models.BooleanField(default=True)
    barrio=models.CharField()
    numeroInmueble=models.IntegerField()
    instruccionesAdicionales=models.CharField()
    estado=models.CharField()
    fechaActualizacion=models.DateTimeField()
