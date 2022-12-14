from database import get_anime_pref, get_league_pref, get_weather_pref
from api_info import *
import math
from datetime import date
def calc_weather(city):
    weather = get_weather(city)
    print(weather)
    temp = weather['temperature']
    humidity = weather['humidity']
    rain_chance = weather['rain_chance']
    if temp > 75:
        temp_factor = math.pow((100-temp), -1) * 100
    elif temp <= 75:
        temp_factor = temp / 75
    
    if humidity <= 60:
        humidity_factor = humidity / 60
    else: 
        humidity_factor = math.pow((100-humidity), -1) * 10
   
    rain_factor = 1 - rain_chance/100

    return (temp_factor + humidity_factor + rain_factor) / 3 
    

def calc_LOL_clash(dates):
    clash_dates = get_LOL_clash()
    print(clash_dates)
    print(dates)
    #if clash_dates['clash_time1'] == 
    
    
def algorithm():
    #print(calc_weather("New York City")) 
    today = date.today()
    calc_LOL_clash(today)

algorithm()