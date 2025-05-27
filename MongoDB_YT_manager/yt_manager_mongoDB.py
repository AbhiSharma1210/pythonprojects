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

yt_collection = db["videos"]

print(yt_collection)

def list_all_videos():
    for video in yt_collection.find():
        print(f"Id: {video['_id']} Name: {video['name']} Time:{video['runTime']}")
    

def add_new_video(name, runTime):
    yt_collection.insert_one({"name": name, "time": runTime})

def replace_video(videoId, name, runTime):
    yt_collection.update_one(
        {'_id': videoId},
        {})

def delete_video(videoId):
    pass

def main():
    while True:
        print("\n Youtube Manager App | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a new youtube video")
        print("3. Replace a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the application")
        
        userChoice = input("Enter your choice: ")
        
        match userChoice:
            case "1":
                list_all_videos()
                
            case "2":
                name = input("Enter the name of video: ")
                runTime = input("Enter the runtime of video: ")
                add_new_video(name, runTime)
                
            case "3":
                videoId = input("Enter the ID of the video to replace: ")
                name = input("Enter the new name of video: ")
                runTime = input("Enter the new runtime of video: ")
                replace_video(videoId, name, runTime)
                
            case "4":
                videoId = input("Enter the ID of the video to delete: ")
                delete_video(videoId)
                
            case "5":
                print("Exiting the application...")
                break
            
            case "6":
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

