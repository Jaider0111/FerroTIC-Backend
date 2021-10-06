from django.db import models


class Horario(models.Model):
    idHorario = models.AutoField(primary_key=True)
    diainicio = models.DateTimeField()
    diafin = models.DateTimeField(default=0)
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField(default=True)