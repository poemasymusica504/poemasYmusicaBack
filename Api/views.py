from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import SingInSerializer
from django.contrib.auth.models import User
from .models import Usuario


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        if user.is_staff or user.is_superuser: return Response('User is no valid')

        usuario = user.usuario_set.first()
        if not usuario: return Response('User has not usuario', status=status.HTTP_400_BAD_REQUEST)

        return Response(usuario.get_user_data())

class SingIn(APIView):
    serializer_class = SingInSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        print(data)
        username = data.get('username', '').lower()
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        if User.objects.filter(username=username).exists():
            return Response({'Error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
        
        if password != confirm_password:
            return Response({'Error': 'Las contraseñas no coinciden'}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'admin_user' in username: 
            user = User.objects.create_superuser(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            return Response(status=status.HTTP_201_CREATED)
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            usuario = Usuario.objects.create(user=user)
        
        return Response(usuario.get_user_data())
    
