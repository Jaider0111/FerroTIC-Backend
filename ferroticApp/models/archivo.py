from django.db import models
from .producto import Producto


class Archivo(models.Model):
    idArchivo = models.BigAutoField(primary_key=True)
    archivo = models.CharField(max_length=200)
    producto = models.ForeignKey(
        Producto, related_name='archivos', on_delete=models.CASCADE)
    tipoContenido = models.CharField(max_length=80)
    vistaPrevia = models.BooleanField(default=False)
