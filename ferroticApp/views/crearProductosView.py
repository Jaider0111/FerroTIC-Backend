from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenObtainSerializer
from rest_framework.views import APIView
from ferroticApp.models import Producto
from rest_framework.permissions import IsAuthenticated


from ferroticApp.serializers.productoSerializer import ProductoSerializer


class CrearProductosView(generics.CreateAPIView):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        return super().post(request, *args, **kwargs)
