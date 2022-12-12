import sqlite3

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)

def setup_tables():
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS logins (username TEXT, uid INTEGER PRIMARY KEY, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS preferences (uid INTEGER PRIMARY KEY, league INTEGER, curfew INTEGER, anime INTEGER, weather INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS user_info (uid INTEGER PRIMARY KEY, city TEXT, favorite_anime TEXT, favorite_weather TEXT)")
    c.close()

def get_password(username):
    c = db.cursor()
    c.execute("SELECT password FROM logins WHERE username = ?", (str(username),) )
    password = c.fetchone()[0]
    c.close()
    return password

def get_uid(username):
    c = db.cursor()
    c.execute("SELECT uid FROM logins WHERE username = ?", (str(username),) )
    uid = c.fetchone()[0]
    c.close()
    return uid

def check_username(username):
    c = db.cursor()
    return_value = c.execute("SELECT username FROM logins WHERE username = ?", (str(username),) )
    try:
        c.fetchone()[0]
        c.close()
        return True
    except:
        c.close()
        return False

def add_user(username, password):
    c = db.cursor()
    # retrieves the number of users which determines the uid
    c.execute("SELECT * FROM logins")
    next_uid = len(c.fetchall())
    # creates new user in table
    c.execute("INSERT INTO logins VALUES(?, ?, ?)", (str(username), int(next_uid), str(password)) )
    db.commit()
    c.close()

def add_pref(uid, league, curfew, anime, weather):
    c = db.cursor()
    c.execute("INSERT INTO preferences VALUES(?, ?, ?, ?, ?) ", (int(uid), int(league), int(curfew), int(anime), int(weather) ))
    db.commit()
    c.close() 

def check_pref(uid):
    c = db.cursor()
    return_value = c.execute("SELECT uid FROM preferences WHERE uid = ?",  (str(uid),))
    try:
        c.fetchone()[0]
        c.close()
        return True 
    except:
        c.close()
        return False

def update_pref(uid, league, curfew, anime, weather):
    c = db.cursor()
    c.execute("UPDATE preferences SET league = ?, curfew = ?, anime = ?, weather = ? WHERE uid = ?", (int(league), int(curfew), int(anime), int(weather), int(uid)))
    db.commit()
    c.close()

def get_league_pref(uid):
    c = db.cursor()
    c.execute("SELECT league FROM preferences WHERE uid = ?", (int(uid),) )
    league_pref = c.fetchone()[0]
    c.close()
    return league_pref

def get_curfew_pref(uid):
    c = db.cursor()
    c.execute("SELECT curfew FROM preferences WHERE uid = ?", (int(uid),) )
    curfew_pref = c.fetchone()[0]
    c.close()
    return curfew_pref

def get_anime_pref(uid):
    c = db.cursor()
    c.execute("SELECT anime FROM preferences WHERE uid = ?", (int(uid),) )
    anime_pref = c.fetchone()[0]
    c.close()
    return anime_pref

def get_weather_pref(uid):
    c = db.cursor()
    c.execute("SELECT weather FROM preferences WHERE uid = ?", (int(uid),) )
    weather_pref = c.fetchone()[0]
    c.close()
    return weather_pref

def add_user_info(uid, city, favorite_anime, favorite_weather):
    c = db.cursor()
    c.execute("INSERT INTO preferences VALUES(?, ?, ?, ?)", (int(uid), str(city), str(favorite_anime), str(favorite_weather)))
    c.close()