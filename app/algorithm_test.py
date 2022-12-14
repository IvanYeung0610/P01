import database as db
import algorithm as algo

db.setup_tables()
db.add_user("test", "1234")
db.add_pref(0, 10, 10, 10)
db.add_user_info(0, "New York", "Naruto")

city = db.get_city(0)
print(algo.calc_weather(city))
print(algo.algorithm(0))
