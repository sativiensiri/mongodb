from pymongo import MongoClient

MONGO_HOST = "10.44.128.98"
MONGO_PORT = 27017
MONGO_DB = "comet"
MONGO_USER = "admin"
MONGO_PASS = "Seagate2020"

connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)

collection = db['rabbitmq']
data = { "name": "Steve", "address": "Highstreet 2" , "Gender": "Male"}

x = collection.insert_one(data)

print(x.inserted_id)

connection.close()