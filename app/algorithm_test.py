import database as db
import algorithm as algo

db.setup_tables()

if not db.check_username("test"):
    db.add_user("test", "1234")

if db.check_pref(0):
    db.update_pref(0, 10, 10, 10)
else:
    db.add_pref(0, 10, 10, 10)

if db.check_user_info(0):
    db.update_user_info(0, "New York", 44511, "Filler")
else:
    db.add_user_info(0, "New York", 44511, "Filler")

print(db.get_city(0))
city = db.get_city(0)
print(algo.calc_weather(city))
print(algo.algorithm(0))
