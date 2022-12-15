import database as db

db.setup_tables()

# db.add_user("Bob", "1234")

# print(db.get_password("Bob"))
# print(db.get_uid("Bob"))
# print(db.check_username("Bob"))
# print(db.check_username("Not Bob"))

# CHECKING ADDING PREFERENCES

print()
print("preferences table exists?:" + str(db.check_pref(0)))
db.add_pref(0, 1, 2, 3)
print(20*"#" + "ADDING PREFERENCES" + 20*"#")

if (db.get_league_pref(0) == 1):
    print("LEAGUE PREF IS CORRECT")
else:
    print("LEAGUE PREF IS INCORRECT. SHOULD BE 1 NOT " + db.get_curfew_pref(0))

if (db.get_anime_pref(0) == 2):
    print("ANIME PREF IS CORRECT")
else:
    print("ANIME PREF IS INCORRECT. SHOULD BE 2 NOT " + db.get_anime_pref(0))

if (db.get_weather_pref(0) == 3):
    print("WEATHER PREF IS CORRECT")
else:
    print("WEATHER PREF IS INCORRECT. SHOULD BE 3 NOT " + db.get_anime_pref(0))

# CHECKING UDATING PREFERENCES

print()
print("preferences table exists?:" + str(db.check_pref(0)))
db.update_pref(0, 2, 4, 6)
print(20*"#" + "UPDATING PREFERENCES" + 20*"#")

if (db.get_league_pref(0) == 2):
    print("LEAGUE PREF IS CORRECT")
else:
    print("LEAGUE PREF IS INCORRECT. SHOULD BE 2 NOT " + db.get_curfew_pref(0))

if (db.get_anime_pref(0) == 4):
    print("ANIME PREF IS CORRECT")
else:
    print("ANIME PREF IS INCORRECT. SHOULD BE 4 NOT " + db.get_anime_pref(0))

if (db.get_weather_pref(0) == 6):
    print("WEATHER PREF IS CORRECT")
else:
    print("WEATHER PREF IS INCORRECT. SHOULD BE 6 NOT " + db.get_anime_pref(0))

#CHECKING ADDING USER_INFO

print()
print("user_info table exists?:" + str(db.check_user_info(0)))
db.add_user_info(0, "New York", 44511, "Rain")
print(20*"#" + "ADDING USER INFO" + 20*"#")

if (db.get_city(0) == "New York"):
    print("CITY IS CORRECT")
else:
    print("CITY IS INCORRECT. SHOULD BE New York NOT " + db.get_city(0))

if (db.get_favorite_anime(0) == 44511):
    print("FAVORITE ANIME IS CORRECT")
else:
    print("FAVORITE ANIME IS INCORRECT. SHOULD BE 44511 NOT " + db.get_favorite_anime(0))

if (db.get_favorite_weather(0) == "Rain"):
    print("FAVORITE WEATHER IS CORRECT")
else:
    print("FAVORITE WEATHER IS INCORRECT. SHOULD BE Rain NOT " + db.get_favorite_weather(0))

#CHECKING UPDATING USER_INFO

print()
print("user_info table exists?:" + str(db.check_user_info(0)))
db.update_user_info(0, "Chicago", 12324, "Sunny")
print(20*"#" + "UPDATING USER INFO" + 20*"#")

if (db.get_city(0) == "Chicago"):
    print("CITY IS CORRECT")
else:
    print("CITY IS INCORRECT. SHOULD BE Chicago NOT " + db.get_city(0))

if (db.get_favorite_anime(0) == 12324):
    print("FAVORITE ANIME IS CORRECT")
else:
    print("FAVORITE ANIME IS INCORRECT. SHOULD BE 12324 NOT " + db.get_favorite_anime(0))

if (db.get_favorite_weather(0) == "Sunny"):
    print("FAVORITE WEATHER IS CORRECT")
else:
    print("FAVORITE WEATHER IS INCORRECT. SHOULD BE Sunny NOT " + db.get_favorite_weather(0))
