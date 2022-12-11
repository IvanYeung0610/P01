from flask import session, Flask, render_template, json
from urllib.request import urlopen, Request
from urllib import request
from datetime import datetime as dt
from api_info import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('api_test.html', 
        #temperature=get_weather("NYC")['temperature'], humidity=get_weather("NYC")['humidity'], rainChance=get_weather("NYC")['rainChance'],
        clashTime1=get_LOL_clash()['clash_time1'], clashTime2=get_LOL_clash()['clash_time2'], 
        anime=get_anime_date(44511)
        )
"""
    #LOL api
    with open('./keys/key_LOL.txt', 'r') as f:
        key_LOL = f.read().strip()
    print(key_LOL)

    URL = f"https://na1.api.riotgames.com/lol/clash/v1/tournaments?api_key={key_LOL}"
    request_site = Request(URL)#bundles url with headers to identify user as not a bot
    #print(URL)#checks for getting correct URL
    response = urlopen(request_site)#grabs the JSON from the page
    data_json = json.loads(response.read())#reads the JSON of the page and turns it into a dictionary
    print(data_json)#checks for correct retrieval of JSON
    time1 = dt.fromtimestamp((int(data_json[1]['schedule'][0]['startTime']) / 1000)).date()
    time2 = dt.fromtimestamp((int(data_json[0]['schedule'][0]['startTime']) / 1000)).date()


    return render_template('api_test.html', clashTime = time1, clashTime2 = time2)

    #MAL api
    with open('./keys/key_MAL.txt', 'r') as f:
        key_MAL = f.read().strip()
    print(key_MAL)

    pref_anime = 41084 #read pref anime to here
    URL = f"https://api.myanimelist.net/v2/anime/{pref_anime}?fields=broadcast"
    headers = {"X-MAL-CLIENT-ID": f"{key_MAL}"}
    request_site = Request(URL, headers = headers)#bundles url with headers to identify user as not a bot
    #print(URL)#checks for getting correct URL
    response = urlopen(request_site)#grabs the JSON from the page
    data_json = json.loads(response.read())#reads the JSON of the page and turns it into a dictionary
    print(data_json)#checks for correct retrieval of JSON 
    anime = data_json['title']
    animeDate = data_json['broadcast']['day_of_the_week'].capitalize()
    return render_template('api_test.html', anime = anime, animeDate = animeDate)
"""
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()