from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
from rest_framework.views import APIView
from ferroticApp.models import ProductoPedido
from rest_framework.permissions import IsAuthenticated


from ferroticApp.serializers import ProductoPedidoSerializer


class CrearProductoPedidoView(generics.CreateAPIView):

    queryset = ProductoPedido.objects.all()
    serializer_class = ProductoPedidoSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        return super().post(request, *args, **kwargs)
