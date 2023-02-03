import json
from django.shortcuts import render
from .models import parameters
from .models import nodeDetails
from django.views.decorators.csrf import csrf_exempt
from django.db.models.functions import Now
import numpy as np
# Create your views here.
from django.http import HttpResponse

DVAR = 10
def dry(request):
# Data collection and fltering
    DVAR = min(15, parameters.objects.filter(raindrop__gte=800).count())
    temp = list(parameters.objects.filter(raindrop__gte=800).values_list('temperature', flat=True).order_by('id')[:DVAR])
    humid = list(parameters.objects.all().values_list('humidity', flat=True).order_by('id')[:DVAR])
    light = list(parameters.objects.all().values_list('light_intensity', flat=True).order_by('id')[:DVAR])
    t1 = parameters.objects.all().values('timestamp').datetimes('timestamp', 'second', 'DESC')[:DVAR]
    time = [time.timestamp()*1000 for time in t1]
    data=np.stack((time, temp, humid, light), axis=0).tolist()
    data[0].insert(0, None)
    data[1].insert(0, 'Temperature')
    data[2].insert(0, 'Humidity')
    data[3].insert(0, 'Light Intensity')
    context={
        'line_data': json.dumps(data)
        }

    return render(request, 'greenhouse_monitoring/templates/dry.html', context)

def rain(request):
# Data collection and fltering
    DVAR = min(15, parameters.objects.filter(raindrop__lte=800).count())
    temp = list(parameters.objects.filter(raindrop__lte=800).values_list('temperature', flat=True).order_by('id')[:DVAR])
    humid = list(parameters.objects.all().values_list('humidity', flat=True).order_by('id')[:DVAR])
    light = list(parameters.objects.all().values_list('light_intensity', flat=True).order_by('id')[:DVAR])
    t1 = parameters.objects.all().values('timestamp').datetimes('timestamp', 'second', 'DESC')[:DVAR]
    time = [time.timestamp()*1000 for time in t1]
    data=np.stack((time, temp, humid, light), axis=0).tolist()
    data[0].insert(0, None)
    data[1].insert(0, 'Temperature')
    data[2].insert(0, 'Humidity')
    data[3].insert(0, 'Light Intensity')
    context={
        'line_data': json.dumps(data)
        }

    return render(request, 'greenhouse_monitoring/templates/rain.html', context)


@csrf_exempt
def receivedata(request):
    if request.method == 'POST':
        nodeID = request.POST['nodeID']
        temp = request.POST['temperature']
        #parameters.objects.insert(temperature = temp)
        humid = request.POST['humidity']
        #parameters.objects.insert(humidity = humid)
        light = request.POST['light_intensity']
        #parameters.objects.create(light_intensity = light)
        raindrop = request.POST['raindrop']
        parameters.objects.create(nodeID = nodeID, temperature = temp, humidity = humid, light_intensity = light, raindrop = raindrop)
        return HttpResponse('POST request completed')

@csrf_exempt
def updatenode(request):
    if request.method == 'POST':
        ID = request.POST['nodeID']
        PIC = request.POST['nodePIC']
        PICContact = request.POST['nodePICContactInfo']
        if nodeDetails.objects.filter(nodeID=ID).exists():
            nodeDetails.objects.filter(nodeID=ID).update(nodePIC = PIC, nodePICContact = PICContact,nodeLastMaintenance=Now())
        else:
            nodeDetails.objects.create(nodeID=ID,nodePIC=PIC,nodePICContact=PICContact)
        return HttpResponse('Node details updated')
