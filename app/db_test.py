import database

# database.setup_tables()
# database.add_user("Bob", "1234")

print(database.get_password("Bob"))
print(database.check_username("Bob"))
print(database.check_username("Not Bob"))
