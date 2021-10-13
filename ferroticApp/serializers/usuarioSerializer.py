from django.db.models import fields
from ferroticApp.models import Usuario
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):

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
            'ubicacion',
            'fotoPerfil',
            'administrador',
            'codigo'
        ]
