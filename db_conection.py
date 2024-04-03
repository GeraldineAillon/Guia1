from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient 

load_dotenv(find_dotenv())

string_conect = os.environ.get("MONGO_URI")
print(string_conect)
CONECCTION_STRING= f"{string_conect}"

client =MongoClient(CONECCTION_STRING) 

main_db=client.guia1

collection = main_db.books