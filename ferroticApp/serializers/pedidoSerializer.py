from ferroticApp.models import Pedido
from rest_framework import serializers


class PedidoSerializer(serializers.ModelSerializer):
    idUsuarioComprador = serializers.IntegerField(
        source="usuarioComprador.idUsuario")
    idUsuarioVendedor = serializers.IntegerField(
        source="usuarioVendedor.idUsuario")

    class Meta:
        model = Pedido
        fields = ['idPedido', 'fechaCompra', 'fechaEntrega', 'total', 'ubicacion', 'idUsuarioComprador', 'idUsuarioVendedor',
                  'telefono', 'nombreReceptor', 'estado', 'numeroArticulos', 'observaciones']
