from django.contrib import admin
from . import models

@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username',)
    raw_id_fields = ('user',)
    list_per_page = 20

@admin.register(models.Poema)
class PoemaAdmin(admin.ModelAdmin):
    list_display = ('escritor', 'titulo', 'tipo',)
    search_fields = ('escritor', 'titulo',)
    list_per_page = 20

@admin.register(models.Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    list_per_page = 20
