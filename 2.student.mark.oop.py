class Student:
    def __init__(self, name, dob, student_id):
        self.name = name
        self.dob = dob
        self.student_id = student_id

class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id

class Grade:
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade

class StudentsAndGrades:
    def __init__(self):
        self.students_data = []
        self.courses_data = []
        self.grades_data = []

    def get_students(self):
        num_students = int(input("Enter the number of students: "))

        for i in range(1, num_students + 1):
            name = input(f"Enter student {i}'s name: ")
            dob = input(f"Enter {name}'s date of birth: ")
            student_id = 'S' + str(i)
            student = Student(name, dob, student_id)
            self.students_data.append(student)

    def get_courses(self):
        num_courses = int(input("Enter the number of courses: "))

        for i in range(1, num_courses + 1):
            name = input(f"Enter course {i}'s name: ")
            course_id = 'C' + str(i)
            course = Course(name, course_id)
            self.courses_data.append(course)

    def get_grades(self):
        grades_choose = int(input("Enter the grade's ID: "))

        for student in self.students_data:
            for course in self.courses_data:
                if course.course_id == 'C' + str(grades_choose):
                    grade = input(f"Enter {student.name}'s grade for {course.name}: ")
                    grade_obj = Grade(student, course, grade)
                    self.grades_data.append(grade_obj)

    def print_grades(self):
        for grade in self.grades_data:
            print(f"Name: {grade.student.name}")
            print(f"ID: {grade.student.student_id}")
            print(f"DOB: {grade.student.dob}")
            print(f"Course: {grade.course.name}")
            print(f"Course ID: {grade.course.course_id}")
            print(f"Grade: {grade.grade}")
            print()

students_and_grades = StudentsAndGrades()
students_and_grades.get_students()
students_and_grades.get_courses()
students_and_grades.get_grades()
students_and_grades.print_grades()