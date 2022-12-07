from flask import Flask, render_template, request, session, redirect, url_for
import os, sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    ret


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
