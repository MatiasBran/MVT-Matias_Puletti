from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from app_MVT_Matias_Puletti.models import Familia
# Create your views here.


def datos_familia(request):
    template=loader.get_template('familia_template.html')
    model = Familia(nombre_familiar=True, edad_familiar= edad_familiar, nacimiento_familiar= nacimiento_familiar)
    model.save()
    render=template.render({'model': model})
    
    return HttpResponse(render)


def listado_familia(request):
    template=loader.get_template('familia_template.html')
    lista_familia = Familia.objects.all()
    render=template.render({'lista_familia': lista_familia})
    return HttpResponse(render)











