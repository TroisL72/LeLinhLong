def students():
    students_data = [
        {"name": "Lisa", "id": 1, "dob": "09/06/2004"},
        {"name": "Jean", "id": 2, "dob": "14/03/2004"},
        {"name": "Barbara", "id": 3, "dob": "05/07/2004"},
        {"name": "Albedo", "id": 4, "dob": "13/09/2004"},
        {"name": "Bennett", "id": 5, "dob": "29/02/2004"}
    ]
    return students_data

def courses():
    courses_data = [
        {"name": "Algebra", "id": 1},
        {"name": "Literature", "id": 2},
        {"name": "History", "id": 3}
    ]
    return courses_data

def grades(students_data, courses_data):
    grades_data = []
    grades_choose = int(input("Enter the grade's id: "))
    for student in students_data:
        for course in courses_data:
            if (course['id'] == grades_choose):
                grade = input(f"Enter {student['name']}'s grade for {course['name']}: ")
                grades_data.append({"student": student, "course": course, "grade": grade})
            else:
                pass
    return grades_data

def print_grades(grades_list):
    print("List of Grades:")
    for grade in grades_list:
        print(f"Name: {grade['student']['name']}")
        print(f"ID: {grade['student']['id']}")
        print(f"DOB: {grade['student']['dob']}")
        print(f"Course: {grade['course']['name']}")
        print(f"Course ID: {grade['course']['id']}")
        print(f"Grade: {grade['grade']}")
        print()


students_list = students()
courses_list = courses()
grades_list = grades(students_list, courses_list)
print_grades(grades_list)


