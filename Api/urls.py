from rest_framework.routers import DefaultRouter
from django.urls import include, re_path as url
from .viewsets import UsuarioViewset, PoemasViewSet

router = DefaultRouter()

router.register(r'^usuario', UsuarioViewset, 'Usuario')
router.register(r'^poema', PoemasViewSet, 'Poema')

