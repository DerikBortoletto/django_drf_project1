from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Derik Bortoletto',
    })

def contact(request):
    return HttpResponse('Contatos') 

def about(request):
    return HttpResponse('Sobre')   