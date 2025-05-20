import json

yt_file = 'youtubeManager/youtube.json'
def load_data():
    try:
        with open(yt_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 
    
def save_data_helper(videos):
    with open(yt_file, 'w') as file:
        json.dump(videos, file)
        print("data saved successfully")

def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']} - Duration: {video['time']}")
    print("*" * 50)

def add_new_video(videos):
    name = input("Enter the name of video: ")
    runTime = input("Enter the runtime of video: ")
    videos.append({"name":name, "time":runTime})
    save_data_helper(videos)

def replace_video(videos):
    try:
        index = int(input("Enter the index of the video to replace: ")) - 1
        if index < 0 or index >= len(videos):
            print("Invalid index. Please try again.")
            return
        name = input("Enter the new name of video: ")
        runTime = input("Enter the new runtime of video: ")
        videos[index] = {"name": name, "time": runTime}
        save_data_helper(videos)
        print("Video replaced successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def delete_video(videos):
    try:
        index = int(input("Enter the index of the video to delete: ")) - 1
        if index < 0 or index >= len(videos):
            print("Invalid index. Please try again.")
            return
        del videos[index]
        save_data_helper(videos)
        print("Video deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

videos = []
def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a new youtube video")
        print("3. Replace a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the application")
        
        userChoice = input("Enter your choice: ")
        
        match userChoice:
            case "1":
                list_all_videos(videos)
                
            case "2":
                add_new_video(videos)
                
            case "3":
                replace_video(videos)
                
            case "4":
                delete_video(videos)
                
            case "5":
                print("Exiting the application...")
                break
            
            case "6":
                print("Invalid choice. Please try again.")
            

if __name__ == "__main__":
    main()