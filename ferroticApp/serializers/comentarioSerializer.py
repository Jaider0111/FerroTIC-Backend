from ferroticApp.models.comentario import Comentario
from rest_framework import serializers

class ComentarioSerializer(serializers.ModelSerializer):
    idProducto=serializers.IntegerField(source='producto.idProducto')
    idUsuario=serializers.IntegerField(source='usuario.idUsuario')
    class Meta:
        model = Comentario
        fields = ['idComentario','idProducto','idUsuario','tipo','contenido','fecha','likes','dislikes']