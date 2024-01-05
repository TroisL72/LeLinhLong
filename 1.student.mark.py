def students():
    students_data = []
    num_students = int(input("Enter the number of students: "))
    
    for i in range(1, num_students + 1):
        name = input(f"Enter student {i}'s name: ")
        dob = input(f"Enter {name}'s date of birth (dd/mm/yyyy): ")
        students_data.append({"name": name, "id": i, "dob": dob})
        
    return students_data

def courses():
    courses_data = []
    num_courses = int(input("Enter the number of courses: "))
    
    for i in range(1, num_courses + 1):
        name = input(f"Enter course {i}'s name: ")
        courses_data.append({"name": name, "id": i})
        
    return courses_data

def grades(students_data, courses_data):
    grades_data = []
    grades_choose = int(input("Enter the grade's id: "))
    
    for student in students_data:
        for course in courses_data:
            if course['id'] == grades_choose:
                grade = input(f"Enter {student['name']}'s grade for {course['name']}: ")
                grades_data.append({"student": student, "course": course, "grade": grade})
                
    return grades_data

def print_grades(grades_list):
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
