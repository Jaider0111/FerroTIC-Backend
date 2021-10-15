from typing import ValuesView
from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ferroticApp.models import Pedido

from datetime import datetime


class ComprarView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        id = kwargs['pk']
        pedido = Pedido.objects.get(idPedido=id)
        pedido.estado = 'ENVIADA'
        pedido.fechaCompra = datetime.now()
        pedido.save()
        return Response({'exitoso': True}, status.HTTP_200_OK)
