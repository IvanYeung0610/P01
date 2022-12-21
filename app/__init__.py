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
        uid = database.get_uid(session["username"])
        if request.method == "GET":
            cities = []
            get_cities(cities)
            #api_info.search_anime(id) <-- SOMETHING IS WRONG WITH THE SPLIT IN API_INFO
            return render_template('preferences.html',
            cities=cities)
        if request.method == "POST":
            if "page2" in request.form and database.get_anime_pref(uid) != 0:
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
                    animeint = name
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
                if (not database.check_pref(uid)):
                    database.add_pref(uid, nba, anime, weather)
                else:
                    database.update_pref(uid, nba, anime, weather)
                
                if (not database.check_user_info(uid)):
                    database.add_user_info(uid, city, 44511, "Filler") # Favorite weather is no longer being used. Will be inserted with filler for now.
                    api_info.get_weather(database.get_city(uid))
                    #print("USER'S CITY: " + database.get_city(uid))
                else:
                    database.update_user_info(uid, city, 44511, "Filler") # Favorite weather is no longer being used. Will be inserted with filler for now.
                    api_info.get_weather(database.get_city(uid))
                    #print("USER'S CITY: " + database.get_city(uid))
                if int(anime) > 0:
                    return render_template('preferences.html',
                    page2=True)
                return redirect(url_for("index"))

@app.route("/logout")
def logout():
    if (not bool(session)):
        return redirect(url_for("index"))
    elif 'username' in session:
        session.clear()
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
            compatibility = algorithm.algorithm(uid)
            grass = algorithm.grass(compatibility)
            airing = database.get_anime_algo_statement(uid)
            city = database.get_city(uid)
            temp = database.get_temperature(city)
            humid = database.get_humidity(city)
            rain = database.get_rain_chance(city)
            return render_template("grass.html", grass=grass, compatibility=compatibility * 100, airing=airing, temp=temp, humid=humid, rain=rain)

@app.route("/weather_details")
def weather_details():
    if (not bool(session)):
        return redirect(url_for("index"))
    else:
        uid = database.get_uid(session["username"])
        if (not database.check_pref(uid)):
            return redirect(url_for("pref"))
        else:
            city = database.get_city(uid)
            temp = str(database.get_temperature(city))
            temp += " " + chr(176)
            humid = str(database.get_humidity(city))
            rain = database.get_rain_chance(city)
            aqi = database.get_aqi(city)
            filler = ", Rating: "
            desc = ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"]
            if (aqi <= 50):
                aqi = str(aqi) + filler + desc[0]
            elif (aqi <= 100):
                aqi = str(aqi) + filler + desc[1]
            elif (aqi <= 150):
                aqi = str(aqi) + filler + desc[2]
            elif (aqi <= 200):
                aqi = str(aqi) + filler + desc[3]
            elif (aqi <= 300):
                aqi = str(aqi) + filler + desc[4]
            else:
                aqi = str(aqi) + filler + desc[5]
            sunrise = database.get_sunrise(city)
            sunset = database.get_sunset(city)
            if (rain <= 25):
                link = "https://cdn-icons-png.flaticon.com/512/3222/3222672.png"
                alt = "sunny"
            elif (rain <= 50):
                link = "https://cdn-icons-png.flaticon.com/512/5822/5822964.png"
                alt = "partly sunny"
            elif (rain <= 75):
                link = "https://cdn-icons-png.flaticon.com/512/899/899718.png"
                alt = "cloudy"
            else:
                link = "https://cdn-icons-png.flaticon.com/512/4088/4088914.png"
                alt = "rainy"
        return render_template("weather.html", temp=temp, humid=humid, rain=str(rain), aqi=aqi, sunrise=sunrise, sunset=sunset, link=link, alt=alt)

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
            return render_template("anime.html", data=data, avg_dur=int(data['average_episode_duration'] / 60))

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
    database.setup_tables()