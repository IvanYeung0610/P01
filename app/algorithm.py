from database import get_anime_pref, get_league_pref, get_weather_pref
from api_info import *
def calc_weather(city):
    weather = get_weather(city)
    temp = weather['temperature']
    humidity = weather['humidity']
    rain_chance = weather['rain_chance']
    temp_factor = None
    humid_factor = None
    rain_factor = None
    if temp > 75:
        temp_factor = (100-temp) / 100
    elif temp < 75:
        temp_factor = temp
    
    
def algorithm(preferences):
    

algorithm()