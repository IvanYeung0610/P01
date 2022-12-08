import sqlite3 

DB_FILE = database.db
db = sqlite3.connect(DB_FILE)
c = db.cursor()

def setup_tables():
    c.execute("create table Logins(username text, uid int, password text)")
    c.execute()

db.commit()
db.close()