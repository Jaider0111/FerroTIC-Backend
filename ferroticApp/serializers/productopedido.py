from ferroticApp.models.horario import productoPedido
from rest_framework import serializers
class productoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = productoPedido
        fields = ['Cantidad', 'Valor']