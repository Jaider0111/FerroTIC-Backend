from django.db.models import fields
from ferroticApp.models import Mensaje
from rest_framework import serializers


class MensajeSerializer(serializers.ModelSerializer):
    idUsuario = serializers.IntegerField(source='usuario.idUsuario')
    idPedido = serializers.IntegerField(source='pedido.idPedido')

    class Meta:
        model = Mensaje
        fields = [
            'idMensaje',
            'idUsuario',
            'idPedido',
            'contenido',
            'fechaEnvio'
        ]
