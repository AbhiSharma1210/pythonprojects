import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
db_name = os.getenv("MONGO_DB_NAME")

mongo_uri = f"mongodb+srv://{username}:{password}@{db_name}.r815rm8.mongodb.net/"

client = MongoClient(mongo_uri)

db = client[db_name]

