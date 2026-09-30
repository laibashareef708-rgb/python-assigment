

students = []

while True:

    print("\n====================================")
    print("     Student Management System      ")
    print("=====================================")
    print("1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Calculate average marks")
    print("5. Delete student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        name = input("Enter your student name: ")
        age = int(input("Enter your student's age: "))
        marks = float(input("Enter your student's marks: "))

        if marks < 0 or marks > 100:
            print("Invalid marks, marks should be between 0 to 100")
        else:
            student = [name, age, marks]
            students.append(student)

            print("Student added successfully!")

    # View student
    elif choice == "2":
        if len(students) == 0:
            print("No students found")
        else:
            print("Student List:")

            for student in students:
                print("Name:", student[0])
                print("Age:", student[1])
                print("Marks:", student[2])
                print()

    # Search student
    elif choice == "3":
        search_name = input("Enter student name to search: ")
        found = False

        for student in students:
            if student[0].lower() == search_name.lower():
                print("Student found:")
                print("Name:", student[0])
                print("Age:", student[1])
                print("Marks:", student[2])
                found = True

        if not found:
            print("Student not found")

    # Calculate average
    elif choice == "4":
        marks1 = float(input("Enter marks of subject 1: "))
        marks2 = float(input("Enter marks of subject 2: "))
        marks3 = float(input("Enter marks of subject 3: "))

        average = (marks1 + marks2 + marks3) / 3

        print("Average Marks:", average)

        if average >= 80:
            print("Grade: A")
        elif average >= 60:
            print("Grade: B")
        elif average >= 40:
            print("Grade: C")
        else:
            print("Grade: Fail")

    # Delete student
    elif choice == "5":
        delete_name = input("Enter student name to delete: ")
        found = False

        for student in students:
            if student[0].lower() == delete_name.lower():
                students.remove(student)
                print("Student deleted successfully")
                found = True
                break

        if not found:
            print("Student not found")

    # Exit
    elif choice == "6":
        print("Exiting from the system")
        break

    else:
        print("Invalid choice. Please enter 1 to 6.")
