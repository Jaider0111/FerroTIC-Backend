from ferroticApp.models.horario import Archivo
from rest_framework import serializers
class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields = ['Archivo', 'Tipodecontenido', 'VistaPrevia',]