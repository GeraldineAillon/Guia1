from pymongo import MongoClient

MONGO_URI =  "mongodb+srv://bddnr1:adminbdd1@bddnr.iq13spn.mongodb.net/?retryWrites=true&w=majority&appName=BDDNR"
client = MongoClient(MONGO_URI)

for db_name in client.list_database_names():
    print(db_name)