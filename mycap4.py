students = []

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def add_student():
    name = input("Enter student name: ")
    math_score = float(input("Enter math score: "))
    science_score = float(input("Enter science score: "))
    english_score = float(input("Enter English score: "))
    student = {
        'name': name,
        'math_score': math_score,
        'science_score': science_score,
        'english_score': english_score
    }
    students.append(student)
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("Student Records:")
        for i, student in enumerate(students, start=1):
            print(f"Student {i}:")
            print("Name:", student['name'])
            print("Math Score:", student['math_score'])
            print("Science Score:", student['science_score'])
            print("English Score:", student['english_score'])
            print("------------------")

def calculate_student_grades():
    if len(students) == 0:
        print("No student records found.")
    else:
        for student in students:
            math_grade = calculate_grade(student['math_score'])
            science_grade = calculate_grade(student['science_score'])
            english_grade = calculate_grade(student['english_score'])
            student['math_grade'] = math_grade
            student['science_grade'] = science_grade
            student['english_grade'] = english_grade

        print("Grades calculated successfully!")

def delete_student():
    if len(students) == 0:
        print("No student records found.")
    else:
        view_students()
        index = int(input("Enter the index of the student to delete: ")) - 1
        if index >= 0 and index < len(students):
            del students[index]
            print("Student deleted successfully!")
        else:
            print("Invalid index.")

def main():
    while True:
        print("\nSchool Administration and Grade Calculation Program")
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Student Grades")
        print("4. Delete Student")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            calculate_student_grades()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
