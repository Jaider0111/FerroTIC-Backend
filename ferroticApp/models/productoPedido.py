from django.db import models
from .producto import Producto
from .pedido import Pedido


class ProductoPedido(models.Model):
    idProductoPedido = models.BigAutoField(primary_key=True)
    producto = models.ForeignKey(
        Producto, related_name='productoPedidos', on_delete=models.CASCADE)
    pedido = models.ForeignKey(
        Pedido, related_name='productoPedidos', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    valor = models.IntegerField()
