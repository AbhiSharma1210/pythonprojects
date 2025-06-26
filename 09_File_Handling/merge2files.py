# program to merge 2 file into a new file.
import os

class unhandledError(Exception):
    "Raise if the auto fix fails"
    pass

def merge_files(first_file, second_file, new_file, retry=False):
    try:
        with open(first_file, 'r') as file1:
            contents1 = file1.read()
        with open(second_file, 'r') as file2:
            contents2 = file2.read()
        with open(new_file, 'w') as file3:
            file3.write(contents1 + "\n" + contents2)
        print(f"Files {first_file} and {second_file} successfully merged into {new_file}")
    except FileNotFoundError as e:
        print(f"Error occured: {e} \nTrying to auto-fix...")
        if not retry:
            try:
                base_folder = "09_File_Handling"
                first_file = os.path.join(base_folder, first_file)
                second_file = os.path.join(base_folder, second_file)
                new_file = os.path.join(base_folder, new_file)
                merge_files(first_file, second_file, new_file, retry=True)
            except Exception:
                raise unhandledError("Auto fix failed unexpectedly.")
        else:
            print("Auto-fix failed. Please run the program from the script's directory.")
            raise
        

def main():
    print("Merge 2 files in a single new file.")
    first_file = input("Enter the name of first file: ").strip()
    if not first_file.lower().endswith(".txt"):
        first_file += '.txt'
    second_file = input("Enter the name of the second file: ").strip()
    if not second_file.lower().endswith(".txt"):
        second_file += '.txt'
    new_file = input("Enter the name of the file that will hold content of 1st and 2nd file: ").strip()
    if not new_file.lower().endswith(".txt"):
        new_file += '.txt'
    merge_files(first_file, second_file, new_file)

if __name__ == "__main__":
    main()