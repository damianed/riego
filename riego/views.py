from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import JsonResponse
from riego.models import Propiedades, Consumodeagua
def index(request):
    props = Propiedades.objects.get(pk=0)
    consumo = Consumodeagua.objects.all()
    context = {
        "propiedades": props,
        "consumo": consumo
    }
    return render(request, 'riego/index.html', context)

def getData(request):
    date = request.GET['date']
    tipo = request.GET['tipo']
    props = Propiedades.objects.get(pk=0)
    consumos = ""
    if tipo == "month":
        year = date.split("-")[0]
        month = date.split("-")[1]
        consumos = Consumodeagua.objects.filter(Fecha__year=year, Fecha__month=month)
    else:
        consumos = Consumodeagua.objects.filter(Fecha__range=(date + " 00:00:00", date + " 23:59:59")).order_by('Fecha')
    context = {
        "propiedades": {
            "Humedad": props.Humedad,
            "Lluvia": props.Lluvia,
            "Fecha": props.Encendido,
        },
        "consumos": {}
    }
    for consumo in consumos:
        context.consumos.append({
            "Litros": consumo.Litros,
            "Fecha": consumo.Fecha
        })
    return JsonResponse(context)