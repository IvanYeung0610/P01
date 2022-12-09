from flask import Flask, render_template, request, session, redirect, url_for
import os, sqlite3

app = Flask(__name__)


app.secret_key = os.urandom(12)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    usr = request.form["user"]
    if request.method == "POST":

        session.permanent = True
        session["username"] = usr
        session['logged_in'] = True

        return redirect(url_for("home"))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session.pop('username', None)
    return redirect(url_for("login"))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/preferences")
def preferences():
    return render_template("preferences.html")

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
