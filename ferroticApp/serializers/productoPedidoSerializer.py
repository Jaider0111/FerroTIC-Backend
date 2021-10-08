from ferroticApp.models.horario import productoPedido
from rest_framework import serializers
class productoPedidoSerializer(serializers.ModelSerializer):
    idProducto = serializers.IntegerField(source= 'producto.idproducto')
    idPedido = serializers.IntegerField(source = "pedido.idPedido")
    class Meta:
        model = productoPedido
        fields = ['idProductoPedido','idPedido', 'idProducto','cantidad', 'valor']