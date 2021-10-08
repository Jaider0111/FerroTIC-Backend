from django.contrib import admin
from .models import Pedido, Comentario, Producto, Usuario, Mensaje, Archivo, ProductoPedido, Horario, Ubicacion

admin.site.register(Horario)
admin.site.register(Ubicacion)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Comentario)
admin.site.register(Mensaje)
admin.site.register(Archivo)
admin.site.register(ProductoPedido)
