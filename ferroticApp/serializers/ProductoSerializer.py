from ferroticApp.models.Producto import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['Id_producto','Nombre','Categoria','Precio','Cantidad','Descripcion','Marca']

