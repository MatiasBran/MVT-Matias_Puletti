from django.contrib import admin
from django.urls import path

from .views import lista_familia

urlpatterns = [
    path('lista-familia/<nom_familiar>/<edad_familiar>/<nacimiento_familiar>/', lista_familia),    
]