from django.db import models
from .producto import Producto
from .usuario import Usuario


class Comentario(models.Model):
    idComentario = models.BigAutoField(primary_key=True)
    producto = models.ForeignKey(
        Producto, related_name='comentarios', on_delete=models.CASCADE)
    usuario = models.ForeignKey(
        Usuario, related_name='comentarios', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=25)
    contenido = models.TextField()
    fecha = models.DateTimeField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
