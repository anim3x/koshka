from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .lib.pogoda import Weather
# import koshka.lib.pogoda as pogoda


# Create your views here.

@csrf_exempt 
def pogoda(request):
    if request.method == 'POST':
        # print(request.body)
        data = json.loads(request.body)
        latitude = data['latitude']
        longitude = data['longitude']
        # print(f"{latitude} {longitude}")
        pogoda = Weather(latitude, longitude)
        weather = pogoda.getWeather()
        # print(weather)
        return JsonResponse(weather)
