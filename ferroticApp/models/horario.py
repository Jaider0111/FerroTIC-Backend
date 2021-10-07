from django.db import models


class Horario(models.Model):
    idHorario = models.BigAutoField(primary_key=True)
    diaInicio = models.DateTimeField()
    diaFin = models.DateTimeField(default=0)
    fechaInicio = models.DateTimeField()
    fechaFin = models.DateTimeField(default=True)
