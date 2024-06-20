from rest_framework import viewsets
from .serializers import UsuarioSerializer, PoemaSelializer
from rest_framework import status
from rest_framework.response import Response
from .models import Usuario, Poema
from .custom_pagination import CustomPagination

class UsuarioViewset(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    pagination_class = None
    queryset = Usuario.objects.all()
    
    def list(self, request):
        try: 
            queryset = self.get_queryset()
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response('Error al listar', status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        
    def update(self, request):
        try:
            data = request.data.copy()
            serializer = self.serializer_class(data=data)
            
        except Exception as e:
            print(e)
            Response('Error al actualizar', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PoemasViewSet(viewsets.ModelViewSet):
    serializer_class = PoemaSelializer
    model_class = Poema
    pagination_class = None
    queryset = Poema.objects.all()
    
    def list(self, request):
        data = request.GET.copy()
        queryset = self.queryset.filter(tipo=data['tipo'])

        try: 
            return CustomPagination(queryset, self.serializer_class).paginate_queryset()
        except Exception as e:
            print(e)
            Response('Error al listar', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        