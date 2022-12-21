from database import *
from api_info import *
import math
from datetime import date, datetime as dt, timedelta
import random
def calc_weather(city):
    get_weather(city)
    temp = get_temperature(city)
    humidity = get_humidity(city)
    rain_chance = get_rain_chance(city) 
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
                #print(difference)
                delta = difference
                #print(dt_object)
                #print(difference)
                #print("delta")
                #print(delta)
                break
    
    if delta == None:
        delta = 0
        #if (f"{x['gdte']}") == str(date.today()):
        #    #print(x)
        #    games_today.append(x)
        #    #print(f"The {x['h']['tc']} {x['h']['tn']} will be playing the {x['v']['tc']} {x['v']['tn']} at {x['stt']} on {x['gdte']}")
    #print(delta)

    if delta < 30 and delta >= 0: #if time till next nba game is < 30 min, calculate %
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

def calc_anime_date(uid, anime_id):
    deets = get_anime_date(anime_id)
    if deets['airing'] == 0:
        add_anime_algo(uid, "Your favorite anime has finished airing. You can watch it whenever you want.")
        return 1 #it's finished! you can watch whenever
    if 'anime_date' in deets and 'anime_time' in deets:
        current_JST = dt.today() + timedelta(hours=14)
        #print(current_JST)
        if current_JST.weekday() == deets['anime_date']: 
            anime_broadcast_time = current_JST.date().strftime('%Y-%m-%d') + " " + deets['anime_time'] #string with anime broadcast date + time
            anime_broadcast_time = dt.strptime(anime_broadcast_time, '%Y-%m-%d %H-%M') #dt object with anime broadcast date + time
            difference = anime_broadcast_time - current_JST 
            difference = difference.total_seconds() / 60 #difference in minutes
            if difference >= 0 and difference < 30:
                add_anime_algo(uid, "An episode of your favorite anime is about to air in " + str(difference) + " minutes.")    
                return difference / 30 
            elif difference < 0 and difference < -60:
                add_anime_algo(uid, "An episode of your favorite anime has aired " + str(-1 * difference) + " minutes ago.")
                return 0 #if it's been less than 1 since episode aired
        else:
            add_anime_algo(uid, "Your favorite anime is not airing today.")
            return 1 #wrong day for anime
    else: 
        return 1 #doesnt have a broadcast time

    #this is the anime airing date for EST
    #abt_est = dt.strptime(anime_broadcast_time, '%Y-%m-%d %H:%M') - (timedelta(hours=14))
    #
    #if weekday_to_integer(deets['anime_date']) == current_day.weekday()""
    
    
    
def algorithm(uid):
    #print(calc_weather("New York City")) 
    #print(calc_weather(replace_space(get_city(uid))) * get_weather_pref(uid) / 10) 

    #print(calc_LOL_clash())
    #print(calc_LOL_clash() * get_league_pref(uid) / 10)
    
    #print(calc_anime_date(44511)) #test using chainsawman
    #p['data'][0irint(calc_anime_date(get_favorite_anime(uid)) * get_anime_pref(uid) / 10) #test using chainsawman
    weather_fac = calc_weather(replace_space(get_city(uid))) * get_weather_pref(uid) / 10
    print("weather: " + str(weather_fac))
    nba_fac = NBA_today(get_NBA()) * get_nba_pref(uid) / 10
    print("nba: " + str(nba_fac))
    anime_fac = calc_anime_date(uid, (get_favorite_anime(uid))) * get_anime_pref(uid) / 10
    print("anime: " + str(anime_fac))
    return((weather_fac + 
            nba_fac + 
            anime_fac) / 3)

def grass(weight):
    yes_no = [0, 1]
    result = random.choices(yes_no, weights=(weight, 1-weight), k = 1)
    if result[0] == 1:
        return "Yes!"
    else:
        return "No!"
    
