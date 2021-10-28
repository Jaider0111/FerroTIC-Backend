from rest_framework import generics, status
from rest_framework.response import Response
from ferroticApp.models import ProductoPedido
from rest_framework.permissions import IsAuthenticated


from ferroticApp.serializers import ProductoPedidoSerializer


class ProductoPedidoRUDView(generics.RetrieveUpdateDestroyAPIView):

    queryset = ProductoPedido.objects.all()
    serializer_class = ProductoPedidoSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({'mensaje': 'elemento borrado'}, status=status.HTTP_200_OK)
