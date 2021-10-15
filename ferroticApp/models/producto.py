from django.db import models


class Producto(models.Model):
    idProducto = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=25)
    precio = models.IntegerField(null=False)
    cantidadDisponible = models.IntegerField(null=True)
    descripcion = models.TextField()
    marca = models.CharField(max_length=35, null=True)
