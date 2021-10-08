from django.db.models import fields
from ferroticApp.models import Usuario
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    idUbicacion = serializers.IntegerField(source='ubicacion.idUbicacion')

    class Meta:
        model = Usuario
        fields = [
            'idUsuario',
            'correo',
            'password',
            'tipoDocumento',
            'numeroDocumento',
            'nombre',
            'fechaNacimiento',
            'telefono',
            'idUbicacion',
            'fotoPerfil',
            'administrador',
            'codigo'
        ]
