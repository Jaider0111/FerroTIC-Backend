from django.urls import path
from ferroticApp.views import UsuarioLoginView, ProductosBusqueda, UsuarioRegistroView, ComprarView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from ferroticApp import views
from django.contrib import admin
from ferroticApp.views import UsuarioLoginView, ProductosBusqueda, UsuarioRegistroView
from rest_framework_simplejwt.views import TokenRefreshView

from ferroticApp.views.crearProductosView import CrearProductosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', UsuarioLoginView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('registro', UsuarioRegistroView.as_view()),
    path('productos', ProductosBusqueda.as_view()),
    path('comprar/<int:pk>', ComprarView.as_view()),
    path('producto/create', CrearProductosView.as_view()),
    path('usuario/<int:pk>/', views.UsuarioDetailView.as_view()),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view()),

]
