from rest_framework_simplejwt.views import TokenViewBase
from ferroticApp.serializers import LoginSerializer


class UsuarioLoginView(TokenViewBase):
    serializer_class = LoginSerializer
