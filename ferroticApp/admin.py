from django.contrib import admin
from .models import Archivo, ProductoPedido, Horario, Ubicacion

admin.site.register(Archivo)
admi.site.register(ProductoPedido)
admin.site.register(Horario)
admin.site.register(Ubicacion)