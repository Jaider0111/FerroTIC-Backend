from ferroticApp.models import Archivo, Producto
from rest_framework import serializers


class ArchivoSerializer(serializers.ModelSerializer):
    idProducto = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Producto.objects.all(), source='producto')

    class Meta:
        model = Archivo
        fields = ['idProducto', 'idArchivo', 'archivo',
                  'tipoContenido', 'vistaPrevia', ]
