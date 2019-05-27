from django.shortcuts import render, HttpResponse
from django.template import loader

def index(request):
    type = "month"
    context = {
        'type': type
    }
    return render(request, 'riego/index.html', context)

def month(request):
    return HttpResponse("Grafica por mes")

def day(request):
    return HttpResponse("Grafica por dia")