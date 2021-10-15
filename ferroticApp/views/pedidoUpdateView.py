from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from ferroticApp.serializers import ProductoPedidoSerializer
from ferroticApp.models import Pedido
from ferroticApp.serializers import PedidoSerializer


class PedidoUpdateView(generics.UpdateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated,)
