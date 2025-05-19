def list_all_videos(videos):
    pass

def add_new_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass



videos = []
while True:
    print("\n Youtube Manager | Choose an option")
    print("1. List all youtube videos")
    print("2. Add a new youtube video")
    print("3. Update a youtube video")
    print("4. Delete a youtube video")
    print("5. Exit the application")
    
    userChoice = input("Enter your choice: ")
    
    match userChoice:
        case "1":
            list_all_videos(videos)
            
        case "2":
            add_new_video(videos)
            
        case "3":
            update_video(videos)
            
        case "4":
            delete_video(videos)
            
        case "5":
            print("Exiting the application...")
            break
        
        case "6":
            print("Invalid choice. Please try again.")