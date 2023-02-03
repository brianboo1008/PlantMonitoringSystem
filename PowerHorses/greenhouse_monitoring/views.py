import json
from django.shortcuts import render
from .models import parameters
from .models import nodeDetails
from django.views.decorators.csrf import csrf_exempt
from django.db.models.functions import Now

# Create your views here.
from django.http import HttpResponse

def temp(request):
# Data collection and fltering
    temp = list(parameters.objects.values_list('temperature').order_by('id')[:10])
    context = { 'line_data': json.dumps(temp)}
    return render(request, 'greenhouse_monitoring/templates/temperature.html', context)

def humid(request):
# Data collection and fltering
    humid = list(parameters.objects.values_list('humidity').order_by('id')[:10])
    context = { 'line_data': json.dumps(humid)}
    return render(request, 'greenhouse_monitoring/templates/humidity.html', context)

def light(request):
# Data collection and fltering
    light = list(parameters.objects.values_list('light_intensity').order_by('id')[:10])
    time = list(parameters.objects.values_list('timestamp').order_by('id')[:10])
    context = {
        'timestamp' : time,
        'line_data': json.dumps(light)}
    return render(request, 'greenhouse_monitoring/templates/lightintensity.html', context)

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
