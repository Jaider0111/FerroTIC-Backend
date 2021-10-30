from django.db import models
from .usuario import Usuario
from .ubicacion import Ubicacion


class Pedido(models.Model):
    idPedido = models.BigAutoField(primary_key=True)
    usuarioComprador = models.ForeignKey(
        Usuario, related_name="compras", on_delete=models.CASCADE)
    usuarioVendedor = models.ForeignKey(
        Usuario, related_name="ventas", on_delete=models.CASCADE)
    fechaCompra = models.DateTimeField(null=True)
    fechaEntrega = models.DateTimeField(null=True)
    total = models.IntegerField(null=True)
    ciudad = models.CharField(max_length=50, null=True)
    direccion = models.CharField(max_length=50, null=True)
    telefono = models.BigIntegerField(null=True)
    nombreReceptor = models.CharField(max_length=70, null=True)
    estado = models.CharField(max_length=30)
    numeroArticulos = models.IntegerField(null=True)
    observaciones = models.TextField(null=True)
