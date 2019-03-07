from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/find?q={}&units=metric&APPID=eda009bb65357426cb3a40c538da6ed4'
    cities = City.objects.all()
    data_weather = []
    message = {'noCity': ''}

    if request.method=='POST':
        print(request.POST)
        if 'name' in request.POST:
            city_name = request.POST['name']
            if requests.get(url.format(city_name)).json()['list']:
                form = CityForm(request.POST)
                form.save()
            else:
                message['noCity'] = 'Not found'

        if 'delete' in request.POST:
            card = City.objects.get(id=int(request.POST['delete']))
            card.delete()
    
    form = CityForm()
    for city in cities:
        r = requests.get(url.format(city.name)).json()
        city_weather = {
            'city': city.name,
            'temperature': r['list'][0]['main']['temp'],
            'description': r['list'][0]['weather'][0]['description'],
            'icon': r['list'][0]['weather'][0]['icon'],
            'id': city.id,
        }
        data_weather.append(city_weather)

    return render(request, 'weather/weather.html', {'data_weather': data_weather, 'form': form, 'message': message})



