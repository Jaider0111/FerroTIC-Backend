from ferroticApp.models import Pedido, Usuario
from rest_framework import serializers


class PedidoSerializer(serializers.ModelSerializer):
    idUsuarioComprador = serializers.PrimaryKeyRelatedField(read_only=True,
                                                            source="usuarioComprador.idUsuario")
    idUsuarioVendedor = serializers.PrimaryKeyRelatedField(read_only=True,
                                                           source="usuarioVendedor.idUsuario")
    usuarioComprador = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Usuario.objects.all())
    usuarioVendedor = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Usuario.objects.all())

    class Meta:
        model = Pedido
        fields = ['idPedido', 'fechaCompra', 'fechaEntrega', 'total', 'ciudad', 'direccion', 'idUsuarioComprador', 'idUsuarioVendedor',
                  'telefono', 'nombreReceptor', 'estado', 'numeroArticulos', 'observaciones', 'usuarioComprador', 'usuarioVendedor']
        depth = 1
