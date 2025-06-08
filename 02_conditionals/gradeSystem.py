# A simple grading system

def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    userNum = input("Please enter a number between 0 and 100: ")
    try:
        studentMark = float(userNum)
        if 0 <= studentMark <= 100:
            print("-"*50)
            print(f"Grade of the student with marks {studentMark} is {assign_grade(studentMark)}")
        else:
            print(f"The number {studentMark} is not between 0 and 100. Please try again")
    except ValueError:
        print("Invalid input. Please try again")
    
if __name__ == "__main__":
    main()