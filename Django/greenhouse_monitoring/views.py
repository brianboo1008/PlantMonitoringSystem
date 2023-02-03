import json
from django.shortcuts import render
from .models import parameters
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse

def temp(request):
# Data collection and fltering
    temp = list(parameters.objects.values_list('temperature').order_by('id')[:10])
    context = { 'line_data': json.dumps(temp)}
    return render(request, '/templates/temperature.html', context)

def humid(request):
# Data collection and fltering
    humid = list(parameters.objects.values_list('humidity').order_by('id')[:10])
    context = { 'line_data': json.dumps(humid)}
    return render(request, '/templates/humidity.html', context)

def light(request):
# Data collection and fltering
    light = list(parameters.objects.values_list('light_intensity').order_by('id')[:10])
    time = list(parameters.objects.values_list('timestamp').order_by('id')[:10])
    context = {
        'line_data': json.dumps(light),
        'timestamp': json.dumps(str(time))
    }
    return render(request, '/templates/lightintensity.html', context)

@csrf_exempt
def receivedata(request):
    if request.method == 'POST':
        temp = request.POST['temperature']
        #parameters.objects.insert(temperature = temp)
        humid = request.POST['humidity']
        #parameters.objects.insert(humidity = humid)
        light = request.POST['light_intensity']
        #parameters.objects.create(light_intensity = light)
        parameters.objects.create(temperature = temp, humidity = humid, light_intensity = light)
        return HttpResponse('POST request completed')