from django.db import models
from .pedido import idPedido
from .usuario import idUsuario

class Ubicacion(models.Model):
    idHorario = models.AutoField(primary_key=True)
    idPedido = models.ForeignKey(idPedido, related_name='Pedido', on_delete=models.CASCADE)
    idUsuario=models.ForeignKey(idUsuario, related_name='Usuario', on_delete=models.CASCADE)
    departamento = models.IntegerField(default=0)
    ciudad = models.DateTimeField()
    direccion = models.BooleanField(default=True)
    barrio=models.CharField()
    numeroinmueble=models.IntegerField()
    instruccionesadicionales=models.CharField()
    estado=models.CharField()
    fechaactualizacion=models.DateTimeField()
