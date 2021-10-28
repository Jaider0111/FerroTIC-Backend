from ferroticApp.models.comentario import Comentario, Producto
from rest_framework import serializers


class ComentarioSerializer(serializers.ModelSerializer):
    idProducto = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Producto.objects.all(), source='producto')
    idUsuario = serializers.IntegerField(source='usuario.idUsuario')

    class Meta:
        model = Comentario
        fields = ['idComentario', 'idProducto', 'idUsuario',
                  'tipo', 'contenido', 'fecha', 'likes', 'dislikes']
