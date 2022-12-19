from flask import Flask, render_template, request, session, redirect, url_for
import os, database, csv, algorithm, api_info

app = Flask(__name__)

app.secret_key = os.urandom(12)
database.setup_tables()

def get_cities(cities):
    with open("cities.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            cities.append(row[1])
        cities.pop(0)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    usr = request.form["user"]
    pswd = request.form["pass"]
    if (not database.check_username(usr)):
        error = "User doesn't exist"
        return render_template("login.html",
        error=error)
    if (database.get_password(usr) != pswd):
        error = "Password incorrect"
        return render_template("login.html",
        error=error)
    if request.method == "POST":
        session.permanent = True
        session["username"] = usr
        session['logged_in'] = True
        uid = database.get_uid(session["username"])
        if (not database.check_pref(uid)):
            return redirect(url_for("pref"))
        else:
            return redirect(url_for("index"))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    usr = request.form["user"]
    pswd = request.form["password"]
    conf = request.form["confirm"]
    if (pswd != conf):
        error = "Passwords do not match"
        return render_template("register.html",
        error=error)
    if (not database.check_username(usr)):
        database.add_user(usr, pswd)
    else:
        error="User already exists"
        return render_template("register.html", error=error)
    if request.method == "POST":
        return redirect(url_for("login"))

@app.route("/preferences", methods=['GET', 'POST'])
def pref():
    if (not bool(session)):
        return redirect(url_for("index"))
    else:
        if request.method == "GET":
            cities = []
            get_cities(cities)
            #api_info.search_anime(id) <-- SOMETHING IS WRONG WITH THE SPLIT IN API_INFO
            return render_template('preferences.html',
            cities=cities)
        if request.method == "POST":
            if "page2" in request.form:
                #if searching for anime name
                if request.form["submit"] == 'Search':
                    search = request.form["search"]
                    searchresult = api_info.search_anime(search)
                    #doesn't currently work without keys
                    return render_template('preferences.html',
                        page2=True,
                        searchresult=searchresult)
                #if picking one 
                else:
                    name = request.form["submit"]
                    #print(searchresult[name])
                    animeint = 44511
                    #name will replace animeint when it is done
                    uid = database.get_uid(session["username"])
                    database.update_favorite_anime(uid, animeint)
                    #get anime using name
                    #print(name)
                    return redirect(url_for("index"))
            else:
                nba = request.form["nba"]
                anime = request.form["anime"]
                weather = request.form["weather"]
                city = request.form["city"]
                #print("VARIABLE HOLDING CITY: " + city)
                uid = database.get_uid(session["username"])
                animeint = 44511
                database.pref(uid, nba, anime, weather)
                database.user_info(uid, city, animeint, "Filler")
                if int(anime) > 0:
                    return render_template('preferences.html',
                    page2=True)
                return redirect(url_for("index"))

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('index'))
    else:
        return "error.html"

@app.route("/grass")
def grass():
    if (not bool(session)):
        return redirect(url_for("index"))
    else:
        uid = database.get_uid(session["username"])
        if (not database.check_pref(uid)):
            return redirect(url_for("pref"))
        else:
            return render_template("grass.html", grass=algorithm.algorithm(uid))

@app.route("/weather_details")
def weather_details():
    if (not bool(session)):
        return redirect(url_for("index"))
    else:
        uid = database.get_uid(session["username"])
        print(uid)
        if (not database.check_pref(uid)):
            return redirect(url_for("pref"))
        else:
            city = database.get_city(uid)
            temp = database.get_temperature(city)
            humid = database.get_humidity(city)
            rain = database.get_rain_chance(city)
            aqi = database.get_aqi(city)
            sunrise = database.get_sunrise(city)
            sunset = database.get_sunset(city)
            '''
            https://cdn-icons-png.flaticon.com/512/3222/3222672.png
            https://cdn-icons-png.flaticon.com/512/5822/5822964.png
            https://cdn-icons-png.flaticon.com/512/899/899718.png
            https://cdn-icons-png.flaticon.com/512/106/106044.png
            https://cdn-icons-png.flaticon.com/512/4088/4088914.png

            Source: https://www.flaticon.com/
            '''
        return render_template("weather.html", temp=temp, humid=humid, rain=rain, aqi=aqi, sunrise=sunrise, sunset=sunset)

@app.route("/nba_details")
def nba_details():
    if (not bool(session)):
        return redirect(url_for("index"))
    else:
        uid = database.get_uid(session["username"])
        if (not database.check_pref(uid)):
            return redirect(url_for("pref"))
        else:
            data = api_info.get_NBA()
            for x in data.copy():
                if x['stt'] == 'Final':
                    data.remove(x)
                    #print("removed")
            #print(data[0])
            return render_template("nba.html", data=data)

@app.route("/anime_details")
def anime_details():
    if (not bool(session)):
        return redirect(url_for("index"))
    else:
        uid = database.get_uid(session["username"])
        if (not database.check_pref(uid)):
            return redirect(url_for("pref"))
        else:
            data = api_info.get_anime_date(database.get_favorite_anime(uid))['data']
            print(data)
            return render_template("anime.html", data=data)

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
    database.setup_tables()