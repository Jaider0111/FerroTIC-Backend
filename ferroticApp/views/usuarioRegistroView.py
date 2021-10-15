import base64
from rest_framework import views, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response

from time import time_ns

from ferroticApp.serializers import UsuarioSerializer
from ferroticApp.services.firebaseService import firebase


class UsuarioRegistroView(views.APIView):

    def post(self, request, *args, **kwargs):
        if "image" in request.data:
            imagen = request.data["image"]
            extension = imagen["name"].split('.')[-1]
            file = base64.b64decode(imagen["data"])
            storage = firebase.storage()
            path = "users/" + str(time_ns()) + extension
            fileInfo = storage.child(path).put(file)
            request.data["fotoPerfil"] = storage.child(
                path).get_url(fileInfo["downloadTokens"])
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokenData = {"correo": request.data["correo"],
                     "password": request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_200_OK)
