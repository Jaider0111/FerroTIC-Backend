from typing import ValuesView
from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from ferroticApp.models import Pedido, pedido
from ferroticApp.models.productoPedido import ProductoPedido
from ferroticApp.serializers import PedidoSerializer

class ComprarView(views.APIView):

    def get(self,request,*args, **kwargs):

        id = kwargs['pk'] 
        pedido = Pedido.objects.get(idPedido = id)
        pedido.estado = 'ENVIADA'
        pedido.save()
        return Response({'exitoso': True}, status.HTTP_200_OK)
        
        