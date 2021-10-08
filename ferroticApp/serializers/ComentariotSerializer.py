from ferroticApp.models.Comentario import Comentario
from rest_framework import serializers

class ComentariotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['Id_Comentario','Tipo','Contenido','Fecha','Likes','Dislikes']