from flask import Flask, render_template, request, session, redirect, url_for
import os, sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":

        session.permanent = True
        session["username"] = user
        session['logged_in'] = True

        return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        return render_template('login.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    session.pop('username', None)


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
