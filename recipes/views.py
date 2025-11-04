from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse('HOME')

def contact(request):
    return HttpResponse('Contatos') 

def about(request):
    return HttpResponse('Sobre')   