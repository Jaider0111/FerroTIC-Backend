from django.conf import settings
from rest_framework import generics, status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ferroticApp.serializers.productoSerializer import ProductoSerializer
from ferroticApp.models import Producto

class ProductoDeleteView(generics.DestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self,request,*args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({'mensaje':'elemento borrado'},status=status.HTTP_200_OK)

 
