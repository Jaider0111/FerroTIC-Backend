from django.db import models
from .usuario import Usuario
from .ubicacion import Ubicacion


class Pedido(models.Model):
    idPedido = models.BigAutoField(primary_key=True)
    usuarioComprador = models.ForeignKey(
        Usuario, related_name="compras", on_delete=models.CASCADE)
    usuarioVendedor = models.ForeignKey(
        Usuario, related_name="ventas", on_delete=models.CASCADE)
    fechaCompra = models.DateTimeField()
    fechaEntrega = models.DateTimeField()
    total = models.IntegerField()
    ubicacion = models.ForeignKey(
        Ubicacion, related_name="pedidos", on_delete=models.CASCADE)
    telefono = models.BigIntegerField()
    nombreReceptor = models.CharField(max_length=70)
    estado = models.CharField(max_length=30)
    numeroArticulos = models.IntegerField()
    observaciones = models.TextField()
