from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Location
from .models import Weather
from .forms import LocationForm
import requests
import json

# Create your views here.
def localFinder(request):
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            locationInput = request.POST.get('location')
            responseLocal = requests.get("http://api.positionstack.com/v1/forward?access_key=8dffbdec1cdc02cc5b5e2cbfb62bdb69&query="+locationInput)
            print(responseLocal)
            if(responseLocal is not None):
                responseLocalJSON=responseLocal.json()
                lat=responseLocalJSON["data"][0]["latitude"]
                long=responseLocalJSON["data"][0]["longitude"]
                print("lat :" + str(lat) + " long :" + str(long))
                Location.objects.create(location_field=locationInput, long_field=long, lat_field=lat)
                responseWeather = requests.get("http://api.weatherapi.com/v1/current.json?key=9b0dbf6ed8964b80a1d122316230407&q="+str(lat)+","+str(long)+"&aqi=no")
                print(responseWeather)
                if(responseWeather is not None):
                    responseWeatherJSON=responseWeather.json()
                    WeatherCon=responseWeatherJSON["current"]["condition"]["text"]
                    WeatherIco=responseWeatherJSON["current"]["condition"]["icon"]
                    WindSpeed=responseWeatherJSON["current"]["wind_kph"]
                    WindDir=responseWeatherJSON["current"]["wind_dir"]
                    Precip=responseWeatherJSON["current"]["precip_mm"]
                    return render(request, "locationFinder.html", {"form": "", "long":long, "lat":lat, "condition":WeatherCon, "icon":WeatherIco, "windsp":str(WindSpeed)+" km/h", "winddir":WindDir, "precip":str(Precip)+" mm", "weathercss":True, "formcss":False})
                else:
                   return render(request, "locationFinder.html", {"form": "", "error":"API error"}) 
            else:
                return render(request, "locationFinder.html", {"form": "", "error":"API error"})
    else:
        form = LocationForm()
    lat="-33.8569"
    long="151.2152"
    return render(request, "locationFinder.html", {"form": form, "long":long, "lat":lat, "weathercss":False, "formcss":True})