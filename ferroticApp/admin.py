from django.contrib import admin
from .models.horario import Horario
from .models.ubicacion import Ubicacion
admin.site.register(Horario)
admin.site.register(Ubicacion)
# Register your models here.
