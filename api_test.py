from flask import session, Flask, render_template, json
from urllib.request import urlopen, Request
from urllib import request

app = Flask(__name__)


@app.route("/")
def home():

    #request_site = Request(getMEME)#bundles url with headers to identify user as not a bot
    #print(URL)#checks for getting correct URL
    response = urlopen(request_site)#grabs the JSON from the page
    data_json = json.loads(response.read())#reads the JSON of the page and turns it into a dictionary
    print(data_json)#checks for correct retrieval of JSON

    return render_template('main.html', image=data_json['body']['image'])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()