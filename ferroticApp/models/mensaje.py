from django.db import models
from .usuario import Usuario
from .pedido import Pedido


class Mensaje(models.Model):
    idMensaje = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(
        Usuario, related_name='mensajes', on_delete=models.CASCADE)
    pedido = models.ForeignKey(
        Pedido, related_name='mensajes', on_delete=models.CASCADE)
    contenido = models.TextField()
    fechaEnvio = models.DateTimeField(auto_now_add=True)
