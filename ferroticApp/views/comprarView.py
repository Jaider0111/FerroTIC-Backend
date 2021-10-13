from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from ferroticApp.models import Pedido, pedido
from ferroticApp.serializers import PedidoSerializer

class Comprar(views.APIView):

    def get(self,request,*args, **kwargs):

        id = kwargs['pk'] 
        pedido = Pedido.objects.get(idPedido = id)