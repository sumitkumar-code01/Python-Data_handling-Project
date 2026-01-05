'''

    Challenge : Student Marks Analyzer
        
        Create a Python program that allows a user to input student
        names along with their marks and then calculates u
        seful statistics.
    
    Program should:

    1. Let the user input multiple students with their marks 
    (name + integer score).
    2. After input is complete, display:
        -Average marks
        -Highest marks and student(s) who scored it
        -Lowest marks and student(s) who scored it
        -Total number of students
'''

# Function to collect student data
def collect_student_data():
    students = {} 
    
    while True:
        name = input("Enter the student name or Stop to Exit: ").strip()
        
        # Check if the user wants to stop inputting data
        if name.lower() == 'stop':
            break
            
        # Basic validation to skip empty names
        if not name:
            print("Name cannot be empty!")
            continue
            
        try:
            score = int(input(f"Enter marks for {name}: "))
            students[name] = score
        except ValueError:
            print("Please enter a valid number for marks.")
            continue
            
    return students

# Function to process and display the final statistics
def main():
    print("--- Student Marks Analyzer ---")
    
    # Collect the Data
    student_list = collect_student_data()
    
    if not student_list:
        print("No data entered.")
        return

    # Total number of students and average marks  
    total_students = len(student_list)
    total_marks = sum(student_list.values())
    average_marks = total_marks / total_students
    
    # Highest aur Lowest  
    max_mark = max(student_list.values())
    min_mark = min(student_list.values())
    
    # List Students who got the highest and lowest marks
    toppers = [name for name, score in student_list.items() if score == max_mark]
    low_scorers = [name for name, score in student_list.items() if score == min_mark]

    # Display the Fianl Output
    print("\n" + "-" * 30)
    print("Detailed Statistics:")
    print(f"Total number of students: {total_students}")
    print(f"Average marks: {average_marks:.2f}")
    print(f"Highest marks: {max_mark} (By: {', '.join(toppers)})")
    print(f"Lowest marks: {min_mark} (By: {', '.join(low_scorers)})")
    print("-" * 30)

# Program ko run karo
if __name__ == "__main__":
    main()