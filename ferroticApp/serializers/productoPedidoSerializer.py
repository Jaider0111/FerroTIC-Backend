from ferroticApp.models import ProductoPedido
from rest_framework import serializers


class ProductoPedidoSerializer(serializers.ModelSerializer):
    idProducto = serializers.IntegerField(source='producto.idProducto')
    idPedido = serializers.IntegerField(source="pedido.idPedido")

    class Meta:
        model = ProductoPedido
        fields = ['idProductoPedido', 'idPedido',
                  'idProducto', 'cantidad', 'valor', "producto"]
        read_only_fields = ["producto"]
        depth = 1
