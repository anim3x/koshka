from django.conf import settings
import requests

class Weather:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.api_key = settings.OPENWEATHER_API_KEY
        self.url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}&units=metric&lang=ru"

    
    def getWeather(self):
        print("Pogoda v dome")
        resp = requests.get(self.url)
        data = resp.json()
        weather = {
            'city': data['name'],
            'temp': round(data['main']['temp'])
        }
        return weather