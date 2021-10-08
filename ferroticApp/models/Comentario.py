from django.db import models
from .user import User

class Comentario(models.Model):
    Id_Comentario = models.AutoField(primary_key=True)
    IdUsuario = models.ForeignKey(User, related_name ='account', on_delete=models.CASCADE)
    Tipo = models.CharField('Nombre', max_length = 25, unique=True)
    Contenido = models.CharField('Nombre', max_length = 100, unique=True)
    Fecha = models.DateTimeField()
    Likes = models.IntegerField(default=0)
    Dislikes = models.IntegerField(default=0)