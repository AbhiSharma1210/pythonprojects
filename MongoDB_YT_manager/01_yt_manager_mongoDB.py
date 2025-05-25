import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")

mongo_url = f"mongodb+srv://{username}:{password}@youtubemanager.r815rm8.mongodb.net/"

client = MongoClient(mongo_url)