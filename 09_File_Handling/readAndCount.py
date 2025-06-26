# A simple program to read a file and count the number of lines and words.

def read_and_count(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            return f"The file has {line_count} number of lines and {word_count} number of words"
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return 

def main():
    # .strip() is used to remove any extra spaces entered by mistake.
    # useful if user entered a space at the end 
    file_path = input("Enter the name of the file, file should be in the same folder as the this code: ").strip() 
    if not file_path.lower().endswith(".txt"):
        file_path += ".txt"
    file_path = f"09_File_Handling/{file_path}"
    print(file_path)
    print("-*-"*20)
    output = read_and_count(file_path)
    if output:
        print(output)
        

if __name__ == "__main__":
    main()