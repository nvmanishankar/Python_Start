import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather_data():
    print('\n please enter the city name:')
    city=input()
    

    request_url='https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'
    weather_data=requests.get(request_url).json()
    print(weather_data)

get_weather_data()