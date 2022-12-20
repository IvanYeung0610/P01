import database as db

db.setup_tables()

# db.add_user("Bob", "1234")

# print(db.get_password("Bob"))
# print(db.get_uid("Bob"))
# print(db.check_username("Bob"))
# print(db.check_username("Not Bob"))

# CHECKING ADDING PREFERENCES

# print()
# print("preferences table exists?:" + str(db.check_pref(0)))
# db.add_pref(0, 1, 2, 3)
# print(20*"#" + "ADDING PREFERENCES" + 20*"#")
#
# if (db.get_league_pref(0) == 1):
#     print("LEAGUE PREF IS CORRECT")
# else:
#     print("LEAGUE PREF IS INCORRECT. SHOULD BE 1 NOT " + db.get_curfew_pref(0))
#
# if (db.get_anime_pref(0) == 2):
#     print("ANIME PREF IS CORRECT")
# else:
#     print("ANIME PREF IS INCORRECT. SHOULD BE 2 NOT " + db.get_anime_pref(0))
#
# if (db.get_weather_pref(0) == 3):
#     print("WEATHER PREF IS CORRECT")
# else:
#     print("WEATHER PREF IS INCORRECT. SHOULD BE 3 NOT " + db.get_anime_pref(0))
#
# # CHECKING UDATING PREFERENCES
#
# print()
# print("preferences table exists?:" + str(db.check_pref(0)))
# db.update_pref(0, 2, 4, 6)
# print(20*"#" + "UPDATING PREFERENCES" + 20*"#")
#
# if (db.get_league_pref(0) == 2):
#     print("LEAGUE PREF IS CORRECT")
# else:
#     print("LEAGUE PREF IS INCORRECT. SHOULD BE 2 NOT " + db.get_curfew_pref(0))
#
# if (db.get_anime_pref(0) == 4):
#     print("ANIME PREF IS CORRECT")
# else:
#     print("ANIME PREF IS INCORRECT. SHOULD BE 4 NOT " + db.get_anime_pref(0))
#
# if (db.get_weather_pref(0) == 6):
#     print("WEATHER PREF IS CORRECT")
# else:
#     print("WEATHER PREF IS INCORRECT. SHOULD BE 6 NOT " + db.get_anime_pref(0))

# #CHECKING ADDING USER_INFO

# print()
# print("user_info table exists?:" + str(db.check_user_info(0)))
# db.add_user_info(0, "New York", 44511, "Rain")
# print(20*"#" + "ADDING USER INFO" + 20*"#")

# if (db.get_city(0) == "New York"):
#     print("CITY IS CORRECT")
# else:
#     print("CITY IS INCORRECT. SHOULD BE New York NOT " + db.get_city(0))

# if (db.get_favorite_anime(0) == 44511):
#     print("FAVORITE ANIME IS CORRECT")
# else:
#     print("FAVORITE ANIME IS INCORRECT. SHOULD BE 44511 NOT " + db.get_favorite_anime(0))

# if (db.get_favorite_weather(0) == "Rain"):
#     print("FAVORITE WEATHER IS CORRECT")
# else:
#     print("FAVORITE WEATHER IS INCORRECT. SHOULD BE Rain NOT " + db.get_favorite_weather(0))

# #CHECKING UPDATING USER_INFO

# print()
# print("user_info table exists?:" + str(db.check_user_info(0)))
# db.update_user_info(0, "Chicago", 12324, "Sunny")
# db.update_city(0, "Alanta")
# db.update_favorite_anime(0, 12324)
# db.update_favorite_weather(0, "Rain")
# print(20*"#" + "UPDATING USER INFO" + 20*"#")

# if (db.get_city(0) == "Chicago"):
#     print("CITY IS CORRECT")
# else:
#     print("CITY IS INCORRECT. SHOULD BE Chicago NOT " + db.get_city(0))

# if (db.get_favorite_anime(0) == 12324):
#     print("FAVORITE ANIME IS CORRECT")
# else:
#     print("FAVORITE ANIME IS INCORRECT. SHOULD BE 12324 NOT " + db.get_favorite_anime(0))

# if (db.get_favorite_weather(0) == "Sunny"):
#     print("FAVORITE WEATHER IS CORRECT")
# else:
#     print("FAVORITE WEATHER IS INCORRECT. SHOULD BE Sunny NOT " + db.get_favorite_weather(0))

## CHECKING ADDING WEATHER

# print()
# db.add_weather_info(0.5, 1.0, 1.5, 2.0, 2.5, 3.0)
# print(20*"#" + "ADDING WEATHER INFO" + 20*"#")

# if (db.get_temperature() == 0.5):
#     print("TEMPERATURE IS CORRECT")
# else:
#     print("TEMPERATURE IS INCORRECT. SHOULD BE 0.5 NOT " + db.get_temperature())

# if (db.get_humidity() == 1.0):
#     print("HUMIDITY IS CORRECT")
# else:
#     print("HUMIDITY IS INCORRECT. SHOULD BE 1.0 NOT " + db.get_humidity())

# if (db.get_rain_chance() == 1.5):
#     print("RAIN CHANCE IS CORRECT")
# else:
#     print("RAIN CHANCE IS INCORRECT. SHOULD BE 1.5 NOT " + db.get_rain_chance())

# if (db.get_aqi() == 2.0):
#     print("AQI IS CORRECT")
# else:
#     print("AQI IS INCORRECT. SHOULD BE 2.0 NOT " + db.get_aqi())

# if (db.get_sunrise() == 2.5):
#     print("SUNRISE IS CORRECT")
# else:
#     print("SUNRISE IS INCORRECT. SHOULD BE 2.5 NOT " + db.get_sunrise())

# if (db.get_sunset() == 3.0):
#     print("SUNSET IS CORRECT")
# else:
#     print("SUNSET IS INCORRECT. SHOULD BE 3.0 NOT " + db.get_sunset())

# #CHECKING ADDING WEATHER WHEN THERE IS ALREADY A ROW

# print()
# db.add_weather_info(1.5, 2.0, 2.5, 3.0, 3.5, 4.0)
# print(20*"#" + "ADDING NEW WEATHER INFO" + 20*"#")

# if (db.get_temperature() == 1.5):
#     print("TEMPERATURE IS CORRECT")
# else:
#     print("TEMPERATURE IS INCORRECT. SHOULD BE 1.5 NOT " + db.get_temperature())

# if (db.get_humidity() == 2.0):
#     print("HUMIDITY IS CORRECT")
# else:
#     print("HUMIDITY IS INCORRECT. SHOULD BE 2.0 NOT " + db.get_humidity())

# if (db.get_rain_chance() == 2.5):
#     print("RAIN CHANCE IS CORRECT")
# else:
#     print("RAIN CHANCE IS INCORRECT. SHOULD BE 2.5 NOT " + db.get_rain_chance())

# if (db.get_aqi() == 3.0):
#     print("AQI IS CORRECT")
# else:
#     print("AQI IS INCORRECT. SHOULD BE 3.0 NOT " + db.get_aqi())

# if (db.get_sunrise() == 3.5):
#     print("SUNRISE IS CORRECT")
# else:
#     print("SUNRISE IS INCORRECT. SHOULD BE 3.5 NOT " + db.get_sunrise())

# if (db.get_sunset() == 4.0):
#     print("SUNSET IS CORRECT")
# else:
#     print("SUNSET IS INCORRECT. SHOULD BE 4.0 NOT " + db.get_sunset())

#CHECKING adding and getting anime_algo

db.add_anime_algo(0, "GO TOUCH GRASS")
print(db.get_anime_algo_statement(0))
