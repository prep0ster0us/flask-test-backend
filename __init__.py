from mongo import init_db, client

print("initializing mongo variables")
init_db()
print(client)