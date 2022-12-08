from flask import session, Flask, render_template, json
from urllib.request import urlopen, Request

app = Flask(__name__)


@app.route("/")
def home():

    request_site = Request("https://api.weatherbit.io/v2.0/current?city=New%20York%20City&key=dadc4ef5d8f84a6687a572237e934b84&units=I")#bundles url with headers to identify user as not a bot
    #print(URL)#checks for getting correct URL
    response = urlopen(request_site)#grabs the JSON from the page
    data_json = json.loads(response.read())#reads the JSON of the page and turns it into a dictionary
    print(data_json)#checks for correct retrieval of JSON
    return render_template('api_test.html', temperature=data_json['data'][0]['temp'], humidity=data_json['data'][0]['rh'], rainChance=data_json['data'])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()