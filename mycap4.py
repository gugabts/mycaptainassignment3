students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    student = {
        'name': name,
        'age': age,
        'grade': grade
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
            print("Age:", student['age'])
            print("Grade:", student['grade'])
            print("------------------")

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
        print("\nSchool Administration Program")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
