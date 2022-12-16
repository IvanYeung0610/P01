from database import *
from api_info import *
import math
from datetime import date
def calc_weather(city):
    weather = get_weather(city)
    #print(weather)
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

   # return {"factor" : (temp_factor + humidity_factor + rain_factor) / 3, "weather" : weather}
    return (temp_factor + humidity_factor + rain_factor) / 3
    

def calc_LOL_clash():
    clash_dates = get_LOL_clash()
    #print(clash_dates)
    #print(dates)
    if clash_dates['clash_time1'] == dt.today():
        return 0
    return 1

def weekday_to_integer(day):
    if day == "Monday":
        return 0
    elif day == "Tuesday":
        return 1
    elif day == "Wednesday":
        return 2
    elif day == "Thursday":
        return 3
    elif day == "Friday":
        return 4
    elif day == "Saturday":
        return 5
    else:
        return 6

def calc_anime_date(anime_id):
    broadcast = weekday_to_integer(get_anime_date(anime_id))
    today = date.today().weekday()
    if broadcast == today:
        return 0
    return 1
    
    
def algorithm(uid):
    #print(calc_weather("New York City")) 
    #print(calc_weather(replace_space(get_city(uid))) * get_weather_pref(uid) / 10) 

    #print(calc_LOL_clash())
    #print(calc_LOL_clash() * get_league_pref(uid) / 10)
    
    #print(calc_anime_date(44511)) #test using chainsawman
    #print(calc_anime_date(get_favorite_anime(uid)) * get_anime_pref(uid) / 10) #test using chainsawman

    return((calc_weather(replace_space(get_city(uid))) * get_weather_pref(uid) / 10) +
            (calc_LOL_clash() * get_league_pref(uid) / 10) +
            (calc_anime_date(get_favorite_anime(uid)) * get_anime_pref(uid) / 10)) / 3

#print(algorithm(0)