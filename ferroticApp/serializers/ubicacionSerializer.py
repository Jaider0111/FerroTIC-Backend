from ferroticApp.models.ubicacion import Ubicacion
from rest_framework import serializers
class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ['departamento', 'ciudad', 'direccion','barrio','numeroInmueble','instruccionesAdicionales','estado','fechaActualizacion']