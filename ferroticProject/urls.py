from django.contrib import admin
from django.urls import path
from ferroticApp.views import UsuarioLoginView, ProductosBusqueda, UsuarioRegistroView, ProductoUpdateView, ProductoDeleteView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', UsuarioLoginView.as_view()),
    path('refresh', TokenRefreshView.as_view()),
    path('registro', UsuarioRegistroView.as_view()),
    path('productos', ProductosBusqueda.as_view()),
    path('producto/update/<int:pk>', ProductoUpdateView.as_view()),
    path('producto/delete/<int:pk>', ProductoDeleteView.as_view()),
]
