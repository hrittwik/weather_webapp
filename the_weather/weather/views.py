import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=bf3d17ed87ffd351bd143812ed51814e'
    city = 'Dhaka'
    
    r = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }

    print(city_weather)
    context = {'city_weather' : city_weather}

    return render(request, 'weather/weather.html', context)
