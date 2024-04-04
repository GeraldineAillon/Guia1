from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient 

load_dotenv(find_dotenv())

password = os.environ.get("MONGO_PWR")

CONECCTION_STRING= f"mongodb+srv://bddnr1:{password}@bddnr.iq13spn.mongodb.net/?retryWrites=true&w=majority&appName=BDDNR"

client =MongoClient(CONECCTION_STRING) 

main_db=client.guia1

collection = main_db.books