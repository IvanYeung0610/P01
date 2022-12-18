from flask import Flask, render_template, request, session, redirect, url_for
import os, database, csv, api_info, algorithm

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
                    '''searchresult = []
                    for x in search:
                        searchresult.append(x)'''
                    return render_template('preferences.html',
                        page2=True,
                        searchresult=searchresult)
                #if picking one 
                else:
                    name = request.form["submit"]
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
                if (not database.check_pref(uid)):
                    database.add_pref(uid, nba, anime, weather)
                else:
                    database.update_pref(uid, nba, anime, weather)
                if (not database.check_user_info(uid)):
                    database.add_user_info(uid, city, 44511, "Filler") # Favorite weather is no longer being used. Will be inserted with filler for now.
                    api_info.get_weather(database.get_city(uid))
                    print("USER'S CITY: " + database.get_city(uid))
                else:
                    database.update_user_info(uid, city, 44511, "Filler") # Favorite weather is no longer being used. Will be inserted with filler for now.
                    api_info.get_weather(database.get_city(uid))
                    print("USER'S CITY: " + database.get_city(uid))
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
        if (not database.check_pref(uid)):
            return redirect(url_for("pref"))
        else:
            city = database.get_city(uid)
            temp = database.get_temperature(city)
            humid = database.get_humidity(city)
            rain = database.get_rain_chance(city)
            print(rain)
            '''
            https://cdn-icons-png.flaticon.com/512/3222/3222672.png
            https://cdn-icons-png.flaticon.com/512/5822/5822964.png
            https://cdn-icons-png.flaticon.com/512/899/899718.png
            https://cdn-icons-png.flaticon.com/512/106/106044.png
            https://cdn-icons-png.flaticon.com/512/4088/4088914.png

        Source: https://www.flaticon.com/
        '''
        return render_template("weather.html", temp=temp, humid=humid, rain=rain)

@app.route("/nba_details")
def nba_details():
    if (not bool(session)):
        return redirect(url_for("index"))
    else:
        uid = database.get_uid(session["username"])
        if (not database.check_pref(uid)):
            return redirect(url_for("pref"))
        else:
            return render_template("nba.html")

@app.route("/anime_details")
def anime_details():
    if (not bool(session)):
        return redirect(url_for("index"))
    else:
        uid = database.get_uid(session["username"])
        if (not database.check_pref(uid)):
            return redirect(url_for("pref"))
        else:
            return render_template("anime.html")

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
    database.setup_tables()