import sqlite3

# A more organized way to handle database connections is to use a context manager
# This ensures that the connection is properly closed after use
def get_db_connection(db_path='yt_manager.db'):
    return sqlite3.connect(db_path)

with get_db_connection() as connection:
    cursor = connection.cursor()
    # execute queries here
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )               
    ''')

def list_all_videos():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM videos")
        rows = cursor.fetchall()
        print("\n")
        print("-" * 50)
        if not rows:
            print("No videos found.")
        else:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Duration: {row[2]}")

def add_new_video(name, runTime):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
                    INSERT INTO videos (name, time)
                    VALUES (?, ?)
                    ''', (name, runTime))
        conn.commit()
        print("\n")
        print("-" * 50)
        print("Video added successfully.")

def replace_video(videosId, name, runTime):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
                    UPDATE videos SET name=?, time=?
                    WHERE id=?
                    ''', (name, runTime, videosId))
        conn.commit()

def delete_video(videosId):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        # Check if the video exists
        cursor.execute('''
                    SELECT * FROM videos WHERE id=?
                    ''', (videosId,))
        row = cursor.fetchone()
        if not row:
            print("\n")
            print("-" * 50)
            print("Video not found.")
            return
        print("\n")
        print("-" * 50)
        cursor.execute('''
                    DELETE FROM videos WHERE id=?
                    ''', (videosId,)) # a comma has to be added to make it a tuple
        conn.commit()
        print("Video deleted successfully.")

def main():
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
