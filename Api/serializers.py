from rest_framework import serializers
from .models import Poema, Usuario, Cancion
from django.contrib.auth.models import User

class UsuarioSerializer( serializers.ModelSerializer ):
    nombres = serializers.CharField(source='user.first_name')
    apellidos = serializers.CharField(source='user.last_name')
    correo = serializers.StringRelatedField(source='user.email')
    username = serializers.StringRelatedField(source='user.usernmae')
    admin = serializers.SerializerMethodField()
    
    def get_admin(self, model):
        return 'admin_' in model.user.username.lower()
    
    class Meta:
        model = Usuario
        fields = '__all__'

class SingInSerializer( serializers.ModelSerializer ):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'email', 'first_name', 'last_name')
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'error': "Las contraseñas no coinciden"})
        if User.objects.filter(username=attrs['username'].lower()).exists():
            raise serializers.ValidationError({'error': 'El usuario ya existe'})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        if 'admin_user' in validated_data['username']:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
        return user
    
class PoemaSelializer( serializers.ModelSerializer ):
    class Meta:
        model = Poema
        fields = '__all__'
        read_only_fields = ['create_at', 'id']