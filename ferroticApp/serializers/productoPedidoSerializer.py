from ferroticApp.models import ProductoPedido, Producto, Pedido
from rest_framework import serializers


class ProductoPedidoSerializer(serializers.ModelSerializer):
    idProducto = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Producto.objects.all(), source='producto')
    idPedido = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Pedido.objects.all(), source='pedido')

    class Meta:
        model = ProductoPedido
        fields = ['idProductoPedido', 'idPedido',
                  'idProducto', 'cantidad', 'valor', "producto"]
        read_only_fields = ["producto"]
        depth = 1
