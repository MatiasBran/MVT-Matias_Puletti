from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.


def lista_familia(request):
    template=loader.get_template('familia_template.html')
    render=template.render({})
    
    return HttpResponse(render)














