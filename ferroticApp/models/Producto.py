from django.db import models

class Producto(models.Model):
    Idproducto=models.AutoField(primary_key=True)
    Nombre=models.CharField('Nombre', max_length = 35, unique=True)
    Categoria=models.CharField('Categoria', max_length = 25, unique=True)
    Precio=models.IntegerField(default=0)
    Cantidad_Disponible=models.IntegerField(default=0)
    Descripcion=models.CharField('Descripcion', max_length = 100, unique=True)
    Marca=models.CharField('Nombre', max_length = 25, unique=True)
