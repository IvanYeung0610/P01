from flask import session, Flask, render_template, json
from urllib.request import urlopen, Request
from urllib import request
from datetime import datetime as dt

app = Flask(__name__)

@app.route("/")
def home():
    
    """
    #weather api
    with open('./keys/key_weatherbit.txt', 'r') as f:
        key_weather = f.read().strip()
    print(key_weather)

    URL = f"https://api.weatherbit.io/v2.0/current?city=New%20York%20City&key={key_weather}&units=I"
    print(URL) 
    response = urlopen(request_site)#grabs the JSON from the page
    data_json = json.loads(response.read())#reads the JSON of the page and turns it into a dictionary
    print(data_json)#checks for correct retrieval of JSON
    return render_template('api_test.html', temperature=data_json['data'][0]['temp'], humidity=data_json['data'][0]['rh'], rainChance=data_json['data'])
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
    #print(dt.fromtimestamp((int(data_json[0]['schedule'][0]['startTime']) / 1000)))
    return render_template('api_test.html', clashTime = dt.fromtimestamp((int(data_json[0]['schedule'][0]['startTime']) / 1000)))

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()