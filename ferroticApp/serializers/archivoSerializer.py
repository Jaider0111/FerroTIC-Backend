from ferroticApp.models.horario import Archivo
from rest_framework import serializers
class ArchivoSerializer(serializers.ModelSerializer):
    idProducto = serializers.IntegerField(source = "producto.idProducto")
    class Meta:
        model = Archivo
        fields = ['idProducto','idArchivo','archivo', 'tipoContenido', 'vistaPrevia',]