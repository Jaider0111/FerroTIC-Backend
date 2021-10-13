
from rest_framework import views, status

from rest_framework.response import Response


from ferroticApp.serializers import ProductoPedidoSerializer
from ferroticApp.services.firebaseService import firebase


class EditarCarrito(views.APIView):

    def post(self, request, *args, **kwargs):
        
        serializer = ProductoPedidoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(data)
            
            return Response(serializer.data,status = status.HTTP_201_CREATED)
    
        return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)   


        



        