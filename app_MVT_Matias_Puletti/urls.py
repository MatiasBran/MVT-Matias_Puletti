from django.contrib import admin
from django.urls import path

from .views import datos_familia, listado_familia

urlpatterns = [
    path('datos-familia/', datos_familia),
    path('listado-familia/', listado_familia)    
]