from database import *
from api_info import *
import math
from datetime import date, datetime as dt, timedelta
def calc_weather(city):
    get_weather(city)
    temp = get_temperature()
    humidity = get_humidity()
    rain_chance = get_rain_chance() 
    #print(rain_chance)
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
    
def NBA_today(data): 

    current_time = dt.today()
    #print(current_time)
    delta = None
    for x in data:
        #print("here")
        #print(f"{x['gdte']}")
        #print(f"{x['stt']}")
        if (f"{x['gdte']}") == str(current_time.date()):
            dt_string = f"{x['gdtutc']} " + f"{x['utctm']}"
            #print(dt_string)
            dt_object = dt.strptime(dt_string, '%Y-%m-%d %H:%M') - (timedelta(hours=5))
            #print(dt_object)
            #print(current_time)
            difference = dt_object - current_time
            difference = difference.total_seconds() / 60
            #print(difference)
            if difference > -60:
                delta = difference
                #print(dt_object)
                #print(difference)
                #print("delta")
                #print(delta)
                break
            else:
                delta = 0
                break
        #if (f"{x['gdte']}") == str(date.today()):
        #    #print(x)
        #    games_today.append(x)
        #    #print(f"The {x['h']['tc']} {x['h']['tn']} will be playing the {x['v']['tc']} {x['v']['tn']} at {x['stt']} on {x['gdte']}")
    #print(delta)

    if delta < 30 and delta > 0: #if time till next nba game is < 30 min, calculate %
        return delta / 30
    elif delta > -60:
        return 0
    else:
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

def calc_anime_date(anime_date):
    if anime_date == date.today().weekday():
        return 0
    return 1
    
    
def algorithm(uid):
    #print(calc_weather("New York City")) 
    #print(calc_weather(replace_space(get_city(uid))) * get_weather_pref(uid) / 10) 

    #print(calc_LOL_clash())
    #print(calc_LOL_clash() * get_league_pref(uid) / 10)
    
    #print(calc_anime_date(44511)) #test using chainsawman
    #p['data'][0irint(calc_anime_date(get_favorite_anime(uid)) * get_anime_pref(uid) / 10) #test using chainsawman
    weather_fac = calc_weather(replace_space(get_city(uid))) * get_weather_pref(uid) / 10
    #print("weather: " + str(weather_fac))
    nba_fac = NBA_today(get_NBA()) * get_nba_pref(uid) / 10
    #print("nba: " + str(nba_fac))
    anime_fac = calc_anime_date(get_anime_date((get_favorite_anime(uid)))) * get_anime_pref(uid) / 10
    #print("anime: " + str(anime_fac))
    return((weather_fac + nba_fac + anime_fac) / 3)
