from django.contrib import admin
from django.urls import path
from ferroticApp.views import UsuarioLoginView, ProductosBusqueda, UsuarioRegistroView, comprarView
from rest_framework_simplejwt.views import TokenRefreshView

from ferroticApp.views.crearProductosView import CrearProductosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', UsuarioLoginView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('registro', UsuarioRegistroView.as_view()),
    path('productos', ProductosBusqueda.as_view()),
    path('comprar', comprarView.Comprar.as_view()),
    path('producto/create', CrearProductosView.as_view())

]
