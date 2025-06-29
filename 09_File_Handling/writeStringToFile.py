# Add a string to a file

def handle_file(file_name, userStr):
    try:
        # a+ means "open and append". It does not create a new file if it doesn't exist.
        # a means "append" a file.
        with open(file_name, 'a') as file:
            userStr = userStr.replace(r'\n','\n')
            file.write(userStr)
            print("Content added to the file successfully. Check the file.")
    except FileNotFoundError:
        print(f"The {file_name} is not found. Please try again.")


def main():
    print("Add a string to a file.")
    file_name = input("Enter the file name: ").strip()
    userStr = input("Enter the string to be added to the file (use \\n to start a new line in the file): ")
    if not file_name.lower().endswith(".txt"):
        file_name += ".txt"
    file_name = f"09_File_Handling/{file_name}"
    handle_file(file_name, userStr)

if __name__ == "__main__":
    main()