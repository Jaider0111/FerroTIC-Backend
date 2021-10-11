from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        isAdmin = self.user.administrador
        data['isAdmin'] = bool(isAdmin)
        return data
