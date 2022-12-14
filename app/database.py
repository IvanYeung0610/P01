import sqlite3

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE, check_same_thread=False)

def setup_tables():
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS logins (username TEXT, uid INTEGER PRIMARY KEY, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS preferences (uid INTEGER PRIMARY KEY, nba INTEGER, anime INTEGER, weather INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS user_info (uid INTEGER PRIMARY KEY, city TEXT, favorite_anime INTEGER, favorite_weather TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS weather_info (city TEXT PRIMARY KEY, temperature REAL, humidity REAL, rain_chance REAL, aqi REAL, sunrise REAL, sunset REAL)")
    c.execute("CREATE TABLE IF NOT EXISTS anime_algo (uid INTEGER PRIMARY KEY, statement TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS nba_algo (statement TEXT)")
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

def pref(uid, nba, anime, weather):
    c = db.cursor()
    c.execute("REPLACE INTO preferences VALUES(?, ?, ?, ?) ", (int(uid), int(nba), int(anime), int(weather) ))
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

def user_info(uid, city, favorite_anime, favorite_weather):
    c = db.cursor()
    c.execute("REPLACE INTO user_info VALUES(?, ?, ?, ?)", (int(uid), str(city), int(favorite_anime), str(favorite_weather)))
    db.commit()
    c.close()

def update_city(uid, city):
    c = db.cursor()
    c.execute("UPDATE user_info SET city = ? WHERE uid = ?", (str(city), int(uid)))
    db.commit()
    c.close()

def update_favorite_anime(uid, favorite_anime):
    c = db.cursor()
    c.execute("UPDATE user_info SET favorite_anime = ? WHERE uid = ?", (str(favorite_anime), int(uid)))
    db.commit()
    c.close()

def update_favorite_weather(uid, favorite_weather):
    c = db.cursor()
    c.execute("UPDATE user_info SET favorite_weather = ? WHERE uid = ?", (str(favorite_weather), int(uid)))
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

def add_weather_info(city, temperature, humidity, rain_chance, aqi, sunrise, sunset):
    c = db.cursor()
    c.execute("DELETE FROM weather_info WHERE city = ?", (str(city),)) #clears all rows from table
    c.execute("INSERT INTO weather_info VALUES(?, ?, ?, ?, ?, ?, ?)", (city, temperature, humidity, rain_chance, aqi, sunrise, sunset))
    db.commit()
    c.close()

def get_temperature(city):
    c = db.cursor()
    c.execute("SELECT temperature FROM weather_info WHERE city = ?", (str(city),))
    temperature = c.fetchone()[0]
    c.close()
    return temperature

def get_humidity(city):
    c = db.cursor()
    c.execute("SELECT humidity FROM weather_info WHERE city = ?", (str(city),))
    humidity = c.fetchone()[0]
    c.close()
    return humidity

def get_rain_chance(city):
    c = db.cursor()
    c.execute("SELECT rain_chance FROM weather_info WHERE city = ?", (str(city),))
    rain_chance = c.fetchone()[0]
    c.close()
    return rain_chance

def get_aqi(city):
    c = db.cursor()
    c.execute("SELECT aqi FROM weather_info WHERE city = ?", (str(city),))
    aqi = c.fetchone()[0]
    c.close()
    return aqi

def get_sunrise(city):
    c = db.cursor()
    c.execute("SELECT sunrise FROM weather_info WHERE city = ?", (str(city),))
    sunrise = c.fetchone()[0]
    c.close()
    return sunrise

def get_sunset(city):
    c = db.cursor()
    c.execute("SELECT sunset FROM weather_info WHERE city = ?", (str(city),))
    sunset = c.fetchone()[0]
    c.close()
    return sunset

def add_anime_algo(uid, statement):
    c = db.cursor()
    c.execute("DELETE FROM anime_algo WHERE uid = ?", (str(uid),)) #clears row of user's previous
    c.execute("INSERT INTO anime_algo VALUES(?, ?)", (str(uid), str(statement)))
    db.commit()
    c.close()

def get_anime_algo_statement(uid):
    c = db.cursor()
    c.execute("SELECT statement FROM anime_algo WHERE uid = ?", (str(uid),))
    statement = c.fetchone()[0]
    c.close()
    return statement

def add_nba_algo(statement):
    c = db.cursor()
    c.execute("DELETE FROM nba_algo" ) #clears all rows
    c.execute("INSERT INTO nba_algo VALUES(?)", (str(statement),))
    db.commit()
    c.close()

def get_nba_algo_statement():
    c = db.cursor()
    c.execute("SELECT statement FROM nba_algo")
    statement = c.fetchone()[0]
    c.close()
    return statement