import sqlite3

DB_FILE = "database.db"
db = sqlite3.connect(DB_FILE)

def setup_tables():
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS logins (username TEXT, uid INTEGER PRIMARY KEY, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS preferences (uid INTEGER PRIMARY KEY, league INTEGER, curfew INTEGER, anime INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS user_info (uid INTEGER PRIMARY KEY, location TEXT, desired_curfew INTEGER, user_id INTEGER)")
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
# Issue with conditions
# def check_username(username):
#     c = db.cursor()
#     return_value = c.execute("SELECT username FROM logins WHERE EXISTS (SELECT username FROM logins WHERE username = ?)", (str(username),) )
#     c.close()
#     return bool(return_value)

def add_user(username, password):
    c = db.cursor()
    # retrieves the number of users which determines the uid
    c.execute("SELECT * FROM logins")
    next_uid = len(c.fetchall())
    # creates new user in table
    c.execute("INSERT INTO logins VALUES(?, ?, ?)", (str(username), str(password), int(next_uid)) )

    db.commit()
    c.close()
