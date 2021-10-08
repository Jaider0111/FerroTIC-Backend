<<<<<<< HEAD
=======

>>>>>>> 7e7978d04f6bb844b4f00c4a205846454e4a2904
from ferroticApp.models.horario import Horario
from rest_framework import serializers
class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['idHorario','diaInicio', 'diaFin', 'fechaInicio','fechaFin']
