from django.db import models


class Horario(models.Model):
    idHorario = models.BigAutoField(primary_key=True)
    diaInicio = models.CharField()
    diaFin = models.CharField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
