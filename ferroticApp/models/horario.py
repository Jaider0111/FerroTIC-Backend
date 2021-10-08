from django.db import models


class Horario(models.Model):
    idHorario = models.BigAutoField(primary_key=True)
    diaInicio = models.CharField(max_length=10)
    diaFin = models.CharField(max_length=10)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
