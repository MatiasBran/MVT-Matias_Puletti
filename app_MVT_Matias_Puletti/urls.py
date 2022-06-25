from django.contrib import admin
from django.urls import path

from app_MVT_Matias_Puletti.views import lista_familia

urlpatterns = [
    path('lista-familia/', lista_familia),    
]