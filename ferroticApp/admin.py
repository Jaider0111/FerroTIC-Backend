from django.contrib import admin
from .models import Comentario
from .models import Producto

admin.site.register(Comentario)
admin.site.register(Producto)