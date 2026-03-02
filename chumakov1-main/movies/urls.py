from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, GenreViewSet, register

router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movie')
router.register('genres', GenreViewSet, basename='genre')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name='register'),
]