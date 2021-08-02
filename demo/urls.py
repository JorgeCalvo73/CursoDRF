from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import BookViewSet

# Creamos el router
router = routers.DefaultRouter()

#Al router le pasamos la url que queremos, y le pasamos un ViewSet
router.register('books', BookViewSet)

urlpatterns = [
    #path('first', views.first),

    path('', include(router.urls))
]