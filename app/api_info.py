from flask import json
from urllib.request import urlopen, Request
from urllib import request
from datetime import datetime as dt, date
from database import add_weather_info
import database

def replace_space(input):
    split_words = input.split(' ')
    output = ""
    for e in split_words:
        output = output + "%20" + e
    return output[3:]

#print(replace_space("test for replace space"))
def get_weather(user_location):
    #weather api
    city = user_location
    try:
        with open('./keys/key_weatherbit.txt', 'r') as f:
            key_weather = f.read().strip()
    except FileNotFoundError:
        print("File containing key for weatherbit does not exist.")
        key_weather = None
    #print(key_weather)
    user_location = replace_space(user_location)
    #print(user_location)
    URL = f"https://api.weatherbit.io/v2.0/current?city={user_location}&key={key_weather}&units=I"
    #print(URL)
    response = urlopen(URL)#grabs the JSON from the page
    data_json = json.loads(response.read())#reads the JSON of the page and turns it into a dictionary
    #print("here " + data_json['data'][0]['precip'])
    #print(data_json)#checks for correct retrieval of JSON
    if data_json['data'][0]['precip'] == None:
        rain_chance = 0
    else:
        rain_chance = data_json['data'][0]['precip']
    #print("User's Location: " + city)
    #print("temperature: " + str(data_json['data'][0]['temp']))
    #print("humidity: " + str(data_json['data'][0]['rh']))
    #print("rain_chance " + str(rain_chance))
    add_weather_info(city, data_json['data'][0]['temp'], data_json['data'][0]['rh'], rain_chance, data_json['data'][0]['aqi'], data_json['data'][0]['sunrise'], data_json['data'][0]['sunset'])
    #print("temperature: " + str(database.get_temperature(city)))
    #print("humidity: " + str(database.get_humidity(city)))
    #print("rain_chance " + str(database.get_rain_chance(city)))

    return None
"""
def get_LOL_clash():
    #LOL api
    try:
        with open('./keys/key_LOL.txt', 'r') as f:
            key_LOL = f.read().strip()
    except FileNotFoundError:
        print("File containing key for RIOT API does not exist")
        key_LOL = None
    #print(key_LOL)

    URL = f"https://na1.api.riotgames.com/lol/clash/v1/tournaments?api_key={key_LOL}"
    request_site = Request(URL)#bundles url with headers to identify user as not a bot
    #print(URL)#checks for getting correct URL
    response = urlopen(request_site)#grabs the JSON from the page
    data_json = json.loads(response.read())#reads the JSON of the page and turns it into a dictionary
    #print(data_json)#checks for correct retrieval of JSON
    if len(data_json) == 2:
        time1 = dt.fromtimestamp((int(data_json[1]['schedule'][0]['startTime']) / 1000)).date()
        time2 = dt.fromtimestamp((int(data_json[0]['schedule'][0]['startTime']) / 1000)).date()
    elif len(data_json) == 1:
        time1 = dt.fromtimestamp((int(data_json[0]['schedule'][0]['startTime']) / 1000)).date()
        time2 = "No clash!"
    elif len(data_json) == 0:
        time1 = "No clash!"
        time2 = "No clash!"
    
    return {"data" : data_json, "clash_time1" : time1, "clash_time2" : time2}
"""

def get_NBA(): #returns list of all games this month
    year = 2022
    mon = date.today().month
    #print(mon)

    match mon: #changes current month (1-12) to month system used by NBA api: Jan = 0 .. . Mar = 3, Sept = 4 ... December = 7
        case 1:
            mon = 0
        case 2:
            mon = 1
        case 3: 
            mon = 2
        case 4:
            mon = 3
        case 9:
            mon = 4
        case 10:
            mon = 5
        case 11:
            mon = 6
        case 12:
            mon = 7 

    url = f"https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/{year}/league/00_full_schedule.json"
    request_site = Request(url)
    response = urlopen(request_site)

    data = json.loads(response.read())
    data = data['lscd'][mon]['mscd']['g']   

    return data

def search_anime(search):
    #MAL api
    try:
        with open('./keys/key_MAL.txt', 'r') as f:
            key_MAL = f.read().strip()
    except FileNotFoundError:
        print("File containing key for My Anime List API does not exist")
        key_MAL = None
    #print(key_MAL)
    search_fixed = replace_space(search)
    #URL = f"https://api.myanimelist.net/v2/anime/{pref_anime}?fields=broadcast"
    URL = f"https://api.myanimelist.net/v2/anime?q={search_fixed}&limit=10"
    headers = {"X-MAL-CLIENT-ID": f"{key_MAL}"}
    request_site = Request(URL, headers = headers)#bundles url with headers to identify user as not a bot
    #print(URL)#checks for getting correct URL
    response = urlopen(request_site)#grabs the JSON from the page
    data_json = json.loads(response.read())#reads the JSON of the page and turns it into a dictionary
    #print("here")
    #print(data_json)#checks for correct retrieval of JSON
    #anime = data_json['title']
    #animeDate = data_json['broadcast']['day_of_the_week'].capitalize()
    return_list = {}
    counter = 0
    for e in data_json['data']:
       values = list(e.values()) #gets rid of data container dict
       for value in values:
        values = list(value.values()) #gets rid of node container dict
        #print(values)
        #anime_name = values[1]
        #print(anime_name)
        return_list[f"{values[1]}"] = values[0]
    #print(return_list)
    return return_list

def get_anime_date(id):
    try:
        with open('./keys/key_MAL.txt', 'r') as f:
            key_MAL = f.read().strip()
    except FileNotFoundError:
        print("File containing key for My Anime List API does not exist")
        key_MAL = None
    #print(key_MAL)
    pref_anime = id #read pref anime to here
    URL = f"https://api.myanimelist.net/v2/anime/{pref_anime}?fields=broadcast"
    headers = {"X-MAL-CLIENT-ID": f"{key_MAL}"}
    request_site = Request(URL, headers = headers)#bundles url with headers to identify user as not a bot
    #print(URL)#checks for getting correct URL
    response = urlopen(request_site)#grabs the JSON from the page
    data_json = json.loads(response.read())#reads the JSON of the page and turns it into a dictionary
    #print(data_json.get("status"))
    anime_date = data_json['broadcast']['day_of_the_week'].capitalize()
    anime_time = data_json['broadcast']['start_time']
    if data_json.get("status") != None:
        if data_json['status'] != "finished_airing":
            airing = 0
    else: airing = 1

    return {"data" : data_json, "anime_date" : anime_date, "anime_time" : anime_time, "airing" : airing}
