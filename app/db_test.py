import database as db

db.setup_tables()

db.add_user("Bob", "1234")

print(db.get_password("Bob"))
print(db.get_uid("Bob"))
print(db.check_username("Bob"))
print(db.check_username("Not Bob"))

# CHECKING ADDING PREFERENCES 

db.add_pref(0, 1, 2, 3, 4)
print()
print(20*"#" + "ADDING PREFERENCES" + 20*"#")

if (db.get_league_pref(0) == 1):
    print("LEAGUE PREF IS CORRECT")
else:
    print("LEAGUE PREF IS INCORRECT. SHOULD BE 1 NOT " + db.get_curfew_pref(0))

if (db.get_curfew_pref(0) == 2):
    print("CURFEW PREF IS CORRECT")
else:
    print("CURFEW PREF IS INCORRECT. SHOULD BE 2 NOT " + db.get_curfew_pref(0))

if (db.get_anime_pref(0) == 3):
    print("ANIME PREF IS CORRECT")
else:
    print("ANIME PREF IS INCORRECT. SHOULD BE 3 NOT " + db.get_anime_pref(0))

if (db.get_weather_pref(0) == 4):
    print("WEATHER PREF IS CORRECT")
else:
    print("WEATHER PREF IS INCORRECT. SHOULD BE 4 NOT " + db.get_anime_pref(0))

# CHECKING UDATING PREFERENCES

db.update_pref(0, 2, 4, 6, 8)
print()
print(20*"#" + "UPDATING PREFERENCES" + 20*"#")

if (db.get_league_pref(0) == 2):
    print("LEAGUE PREF IS CORRECT")
else:
    print("LEAGUE PREF IS INCORRECT. SHOULD BE 1 NOT " + db.get_curfew_pref(0))

if (db.get_curfew_pref(0) == 4):
    print("CURFEW PREF IS CORRECT")
else:
    print("CURFEW PREF IS INCORRECT. SHOULD BE 2 NOT " + db.get_curfew_pref(0))

if (db.get_anime_pref(0) == 6):
    print("ANIME PREF IS CORRECT")
else:
    print("ANIME PREF IS INCORRECT. SHOULD BE 3 NOT " + db.get_anime_pref(0))

if (db.get_weather_pref(0) == 8):
    print("WEATHER PREF IS CORRECT")
else:
    print("WEATHER PREF IS INCORRECT. SHOULD BE 4 NOT " + db.get_anime_pref(0))