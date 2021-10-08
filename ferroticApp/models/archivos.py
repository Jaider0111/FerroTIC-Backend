from django.db import models


class Archivo(model.Model):
    idArchivo = models.AutoField(primary_key=True)
    Archivo = models.CharField() 
    idProducto = models.ForeignKey(idProducto, related_name='Producto', on_delete=models.CASCADE)
    tipodecontenido = models.CharField()
    vistaprevia = models.BooleanField(default=True)