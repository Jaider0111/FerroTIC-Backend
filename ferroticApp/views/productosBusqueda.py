from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from ferroticApp.models import Producto
from ferroticApp.serializers import ProductoSerializer


class ProductosBusqueda(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated,)

    search_fields = ['nombre']
    ordering_fields = ['nombre', 'categoria', 'precio']
    filterset_fields = {
        'categoria': ['iexact', 'exact'],
        'precio': ['gte', 'lte', 'exact', 'range']
    }
