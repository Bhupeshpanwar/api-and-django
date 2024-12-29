from django.shortcuts import render
from django.http import HttpResponse
import requests

# Replace 'your_api_key_here' with your actual API key
API_KEY = ''

def index(request):
    weather_data = None
    error_message = None

    # Check if the form is submitted with a location
    if request.method == 'GET' and 'location' in request.GET:
        location = request.GET.get('location', '')
        if location:
            try:
                # Fetch weather data from the OpenWeatherMap API
                url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
                response = requests.get(url)
                data = response.json()

                if response.status_code == 200:
                    weather_data = {
                        'location': data['name'],
                        'temperature': data['main']['temp'],
                        'description': data['weather'][0]['description'],
                        'icon': data['weather'][0]['icon']
                    }
                else:
                    error_message = data.get('message', 'Could not retrieve weather data.')
            except Exception as e:
                error_message = 'An error occurred while fetching weather data.'

    return render(request, 'location.html', {'weather_data': weather_data, 'error_message': error_message})
