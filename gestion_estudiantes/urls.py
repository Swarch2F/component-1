from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, EstudianteViewSet

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'estudiantes', EstudianteViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 