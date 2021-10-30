from typing import ValuesView
from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ferroticApp.models import Pedido, Usuario

from datetime import datetime


class ComprarView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        id = kwargs['pk']
        pedido = Pedido.objects.get(idPedido=id)
        pedido.estado = 'ENVIADA'
        pedido.fechaCompra = datetime.now()
        pedido.save()
        pedidoN = None
        pedidoN = Pedido(
            usuarioComprador=Usuario.objects.get(
                pk=pedido.usuarioComprador.idUsuario),
            usuarioVendedor=Usuario.objects.get(pk=12),
            estado='CARRITO',
        )
        pedidoN.save()
        return Response({'exitoso': True, 'pedido': pedidoN.idPedido}, status.HTTP_200_OK)
