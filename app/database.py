import sqlite3

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)

def setup_tables():
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS logins (username TEXT, uid INTEGER PRIMARY KEY, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS preferences (uid INTEGER PRIMARY KEY, NBA INTEGER, anime INTEGER, weather INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS user_info (uid INTEGER PRIMARY KEY, city TEXT, favorite_anime INTEGER, favorite_weather TEXT)")
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

def add_pref(uid, nba, anime, weather):
    c = db.cursor()
    c.execute("INSERT INTO preferences VALUES(?, ?, ?, ?) ", (int(uid), int(nba), int(anime), int(weather) ))
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

def update_pref(uid, nba, anime, weather):
    c = db.cursor()
    c.execute("UPDATE preferences SET nba = ?, anime = ?, weather = ? WHERE uid = ?", (int(nba), int(anime), int(weather), int(uid)))
    db.commit()
    c.close()

def get_nba_pref(uid):
    c = db.cursor()
    c.execute("SELECT nba FROM preferences WHERE uid = ?", (int(uid),) )
    nba_pref = c.fetchone()[0]
    c.close()
    return nba_pref

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
    c.execute("INSERT INTO user_info VALUES(?, ?, ?, ?)", (int(uid), str(city), int(favorite_anime), str(favorite_weather)))
    db.commit()
    c.close()

def check_user_info(uid):
    c = db.cursor()
    c.execute("SELECT uid FROM user_info WHERE uid = ?",  (str(uid),))
    try:
        c.fetchone()[0]
        c.close()
        return True
    except:
        c.close()
        return False

def update_user_info(uid, city, favorite_anime, favorite_weather):
    c = db.cursor()
    c.execute("UPDATE user_info SET city = ?, favorite_anime = ?, favorite_weather = ? WHERE uid = ?", (str(city), int(favorite_anime), str(favorite_weather), int(uid)))
    db.commit()
    c.close()

def get_city(uid):
    c = db.cursor()
    c.execute("SELECT city FROM user_info WHERE uid = ?", (str(uid),))
    city = c.fetchone()[0]
    c.close()
    return city

def get_favorite_anime(uid):
    c = db.cursor()
    c.execute("SELECT favorite_anime FROM user_info WHERE uid = ?", (str(uid),))
    favorite_anime = c.fetchone()[0]
    c.close()
    return favorite_anime

def get_favorite_weather(uid):
    c = db.cursor()
    c.execute("SELECT favorite_weather FROM user_info WHERE uid = ?", (str(uid),))
    favorite_weather = c.fetchone()[0]
    c.close()
    return favorite_weather
