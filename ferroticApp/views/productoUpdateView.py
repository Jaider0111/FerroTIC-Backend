from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ferroticApp.models.producto import Producto
from ferroticApp.serializers.productoSerializer import ProductoSerializer


class ProductoUpdateView(generics.UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
