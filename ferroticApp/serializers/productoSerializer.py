from ferroticApp.models import Producto
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombre', 'categoria',
                  'precio', 'cantidadDisponible', 'descripcion', 'marca']
