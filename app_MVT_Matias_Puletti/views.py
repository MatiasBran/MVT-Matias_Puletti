from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from app_MVT_Matias_Puletti.models import Familia
# Create your views here.


def lista_familia(request, nom_familiar, edad_familiar, nacimiento_familiar):
    template=loader.get_template('familia_template.html')
    model = Familia(nombre_familiar=nom_familiar, edad_familiar= edad_familiar, nacimiento_familiar= nacimiento_familiar)
    model.save()
    render=template.render({'model': model})
    
    return HttpResponse(render)














