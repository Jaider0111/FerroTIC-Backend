from django.db import models


class Horario(models.Model):
    idHorario = models.BigAutoField(primary_key=True)
    diaInicio = models.CharField()
    diaFin = models.DateTimeField(default=0)
    horaInicio = models.TimeField()
    fechaFin = models.DateTimeField(default=True)