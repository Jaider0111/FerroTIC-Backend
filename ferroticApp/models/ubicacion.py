from django.db import models


class Ubicacion(models.Model):
    idUbicacion = models.BigAutoField(primary_key=True)
    departamento = models.CharField(30)
    ciudad = models.CharField(30)
    direccion = models.CharField(60)
    barrio=models.CharField(60)
    numeroInmueble=models.IntegerField()
    instruccionesAdicionales=models.TextField()
    estado=models.CharField()
    fechaActualizacion=models.DateTimeField()
