from django.db import models


class productoPedido(model.Model):
    idproductoPedido = models.AutoField(primary_key=True)
    idProducto = models.ForeignKey(idProducto, related_name='Producto', on_delete=models.CASCADE)
    idPedido = models.ForeignKey(idPedido, related_name='Pedido', on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    Valor = models.IntegerField()