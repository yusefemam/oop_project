# oop_project
class Student:
    students = 0

    def __init__(self, name, age, gpa, courses):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.courses = courses
        Student.students += 1

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, GPA: {self.gpa}, Courses: {', '.join(self.courses)}"


students = {
    "yusef": Student("Yusef Emam Abdelfattah", 19, 3.1, [
        "Intro to linguistics",
        "Linear algebra",
        "AI",
        "Programming",
        "Phonetics",
        "Communication skills",
        "Computer skills",
        "Arabic skills"
    ]),
    "abdelrahman": Student("Abdelrahman Mohamed Eldardery", 18, 2.8, [
        "Intro to linguistics",
        "Linear algebra",
        "AI",
        "Programming",
        "Phonetics",
        "Communication skills",
        "Computer skills",
        "Arabic skills"
    ])
}

user = input("Enter your username: ").strip().lower()

if user in students:
    student = students[user]
    ask = input(
        "Enter what you want to show? (e.g., courses, age, name, gpa or All?): ").strip().lower()

    if ask == "courses":
        for i, course in enumerate(student.courses):
            print(f"{i + 1}. {course}")
    elif ask == "age":
        print(student.age)
    elif ask == "name":
        first = input(
            "Do you want to view just first and middle name or fullname? ").strip().lower()
        if first == "first and middle":
            first_and_middle_name = f"{student.name.split()[0]} {student.name.split()[1]}"
            print(first_and_middle_name)
        elif first == "fullname":
            print(student.name)
        else:
            print("Invalid option for name.")
    elif ask == "gpa":
        print(student.gpa)
    elif ask == "all":
        print(student)
    else:
        print("Invalid option. Please try again.")
else:
    add = input(
        "User not found. Do you want to add a new student? (yes/no): ").strip().lower()
    if add == "yes":
        name = input("Enter student's name: ").strip()
        age = int(input("Enter student's age: ").strip())
        gpa = float(input("Enter student's GPA: ").strip())
        courses = input(
            "Enter student's courses (comma separated): ").strip().split(", ")
        students[user] = Student(name, age, gpa, courses)
        print(f"Student {name} added successfully!")
        print(f"{students[user]}")
    else:
        print("No changes made.")
