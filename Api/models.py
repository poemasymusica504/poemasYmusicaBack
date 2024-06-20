from typing import Iterable
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from rest_framework.authtoken.models import Token

class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.get_full_name()
    
    def get_user_data(self):
        token, created = Token.objects.get_or_create(user=self.user)

        return {
            'id': self.id,
            'nombre_completo': self.user.get_full_name(),
            'token': token.key,
            'username': self.user.username,
            'user_id': self.user.pk,
            'admin': 'admin_' in self.user.username.lower(),
        }


class Poema(models.Model):
    user_id_favorito = models.ManyToManyField(User, null=True, blank=True)
    escritor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    resumen = models.CharField(max_length=200)
    poema = models.TextField(max_length=5000)
    img_url = models.URLField()
    tipo_choices = [
        ("amor", "Amor"),
        ("vida", "Vida"),
    ]
    tipo = models.CharField(max_length=15, choices=tipo_choices, verbose_name="Tipo de Poema", null=True)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Cancion(models.Model):
    nombre = models.CharField(max_length=50)
    letra = models.TextField(max_length=1000)
    img_url = models.URLField()
    url_song = models.TextField()
    user_id_favorito = ArrayField(models.IntegerField(), blank=True, default=list)
    create_at = models.DateField(auto_now_add=True)