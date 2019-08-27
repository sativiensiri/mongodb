from pymongo import MongoClient

db = MongoClient('10.44.128.98:27017')

databaseList = db.list_database_names()
print(databaseList)
print(db[databaseList[0]])



