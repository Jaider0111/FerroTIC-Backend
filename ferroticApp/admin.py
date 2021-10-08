from django.contrib import admin
from .models import Usuario, Mensaje, Archivo, ProductoPedido, Horario, Ubicacion

admin.site.register(Usuario)
admin.site.register(Mensaje)
admin.site.register(Archivo)
admi.site.register(ProductoPedido)
admin.site.register(Horario)
admin.site.register(Ubicacion)