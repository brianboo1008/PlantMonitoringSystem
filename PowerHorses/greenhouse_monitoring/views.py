from django.shortcuts import render
from .models import parameters
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def status(request):
	param = parameters.objects.all()
	template = loader.get_template("testing/status.html")
	context = { 'parameters' : param, }
	return HttpResponse(template.render(context,request))

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