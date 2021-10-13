from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from ferroticApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('usuario/<int:pk>/', views.UsuarioDetailView.as_view()),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view()),
]