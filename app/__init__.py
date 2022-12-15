from flask import Flask, render_template, request, session, redirect, url_for
import os, database, csv, api_info

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
    return render_template('home.html')

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
        return redirect(url_for("home"))

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
        return render_template("register.html")
    if request.method == "POST":
        return redirect(url_for("login"))

@app.route("/preferences", methods=['GET', 'POST'])
def pref():
    if request.method == "GET":
        cities = []
        get_cities(cities)
        #api_info.search_anime(id) <-- SOMETHING IS WRONG WITH THE SPLIT IN API_INFO
        return render_template('preferences.html',
        cities=cities)
    if request.method == "POST":
        if "page2" in request.form:
            search = request.form["search"]
            searchresult = api_info.search_anime(search)
            return render_template('preferences.html',
                page2=True,
                searchresult=searchresult)
        else:
            league = request.form["league"]
            anime = request.form["anime"]
            weather = request.form["weather"]
            city = request.form["city"]
            uid = database.get_uid(session["username"])

            if (not database.check_pref(uid)):
                database.add_pref(uid, league, anime, weather)
            else:
                database.update_pref(uid, league, anime, weather)

            if int(anime) > 0:
                return render_template('preferences.html',
                page2=True)
            
        if (not database.check_user_info(uid)):
            database.add_user_info(uid, city, 44511, "Filler") # Favorite weather is no longer being used. Will be inserted with filler for now.
        else:
            database.update_user_info(uid, city, 44511, "Filler") # Favorite weather is no longer being used. Will be inserted with filler for now.
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session.pop('username', None)
    return redirect(url_for("login"))

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/grass")
def grass():
    return render_template("grass.html")

@app.route("/info")
def info():
    return render_template("info.html")

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
    database.setup_tables()
