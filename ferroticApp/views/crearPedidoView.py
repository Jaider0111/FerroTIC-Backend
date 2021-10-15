from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ferroticApp.models import Pedido
from ferroticApp.serializers import PedidoSerializer


class CrearPedidoView(generics.CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = (IsAuthenticated)
