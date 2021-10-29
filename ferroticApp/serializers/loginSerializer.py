from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ferroticApp.models import Pedido, Usuario


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        isAdmin = bool(self.user.administrador)
        data['isAdmin'] = isAdmin
        if not isAdmin:
            pedido = None
            try:
                pedido = Pedido.objects.get(
                    usuarioComprador__idUsuario=self.user.idUsuario, estado='CARRITO')
            except:
                pedido = Pedido(
                    usuarioComprador=Usuario.objects.get(
                        pk=self.user.idUsuario),
                    usuarioVendedor=Usuario.objects.get(pk=12),
                    estado='CARRITO',
                )
                pedido.save()
            data['pedido'] = pedido.idPedido
        return data
