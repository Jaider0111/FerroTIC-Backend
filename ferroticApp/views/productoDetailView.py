from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from ferroticApp.models.producto import Producto
from ferroticApp.serializers.productoSerializer import Producto, ProductoSerializer


class ProductoDetailView(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated,)

    def get(sefl, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
