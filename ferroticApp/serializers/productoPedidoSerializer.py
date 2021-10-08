from ferroticApp.models import ProductoPedido
from rest_framework import serializers


class ProductoPedidoSerializer(serializers.ModelSerializer):
    idProducto = serializers.IntegerField(source='producto.idproducto')
    idPedido = serializers.IntegerField(source="pedido.idPedido")

    class Meta:
        model = ProductoPedido
        fields = ['idProductoPedido', 'idPedido',
                  'idProducto', 'cantidad', 'valor']
