from ferroticApp.models.horario import Horario
from rest_framework import serializers
class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['diaInicio', 'diaFin', 'fechaInicio','fechaFin']