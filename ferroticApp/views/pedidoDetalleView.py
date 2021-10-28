from typing import ValuesView
from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ferroticApp.models import Pedido, ProductoPedido
from ferroticApp.serializers import PedidoSerializer, ProductoPedidoSerializer


class PedidoDetalleView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        pedido = Pedido.objects.get(
            usuarioComprador__idUsuario=id, estado='CARRITO')
        pedidoR = PedidoSerializer(pedido).data
        productos = pedido.productoPedidos.all()
        pedidoR["productos"] = ProductoPedidoSerializer(
            productos,  many=True).data
        return Response(pedidoR, status.HTTP_200_OK)
