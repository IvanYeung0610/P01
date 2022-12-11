from flask import json
from urllib.request import urlopen, Request
from urllib import request
from datetime import datetime as dt
    
def get_weather(user_location):
    #weather api
    with open('./keys/key_weatherbit.txt', 'r') as f:
        key_weather = f.read().strip()
    #print(key_weather)

    URL = f"https://api.weatherbit.io/v2.0/current?city={user_location}&key={key_weather}&units=I"
    #print(URL) 
    response = urlopen(URL)#grabs the JSON from the page
    data_json = json.loads(response.read())#reads the JSON of the page and turns it into a dictionary
    #print(data_json)#checks for correct retrieval of JSON
    return {"temperature" : data_json['data'][0]['temp'], "humidity" : data_json['data'][0]['rh'], "rain_chance" : data_json['data'][0]['precip']}

def get_LOL_clash():
    #LOL api
    with open('./keys/key_LOL.txt', 'r') as f:
        key_LOL = f.read().strip()
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
        
    return {"clash_time1" : time1, "clash_time2" : time2}

def search_anime(search):
    #MAL api
    with open('./keys/key_MAL.txt', 'r') as f:
        key_MAL = f.read().strip()
    print(key_MAL)

    pref_anime = 41084 #read pref anime to here
    #URL = f"https://api.myanimelist.net/v2/anime/{pref_anime}?fields=broadcast"
    URL = f"https://api.myanimelist.net/v2/anime?q={search}&limit=2"
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
        print(values)
        #anime_name = values[1]
        #print(anime_name)
        return_list[f"{values[1]}"] = values[0]
    print(return_list)
    return return_list