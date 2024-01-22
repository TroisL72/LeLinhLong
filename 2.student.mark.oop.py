class Student:
    def __init__(self, name, dob, student_id):
        self.__name = name
        self.__dob = dob
        self.__student_id = student_id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_student_id(self):
        return self.__student_id

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"ID: {self.__student_id}")
        print(f"DOB: {self.__dob}")


class Course:
    def __init__(self, name, course_id):
        self.__name = name
        self.__course_id = course_id

    def get_name(self):
        return self.__name

    def get_course_id(self):
        return self.__course_id

    def display_info(self):
        print(f"Course: {self.__name}")
        print(f"Course ID: {self.__course_id}")


class Grade:
    def __init__(self, student, course, grade):
        self.__student = student
        self.__course = course
        self.__grade = grade

    def display_info(self):
        self.__student.display_info()
        self.__course.display_info()
        print(f"Grade: {self.__grade}")
        print()


class StudentsAndGrades:
    def __init__(self):
        self.__students_data = []
        self.__courses_data = []
        self.__grades_data = []

    def get_students(self):
        num_students = int(input("Enter the number of students: "))

        for i in range(1, num_students + 1):
            name = input(f"Enter student {i}'s name: ")
            dob = input(f"Enter {name}'s date of birth: ")
            student_id = 'S' + str(i)
            student = Student(name, dob, student_id)
            self.__students_data.append(student)

    def get_courses(self):
        num_courses = int(input("Enter the number of courses: "))

        for i in range(1, num_courses + 1):
            name = input(f"Enter course {i}'s name: ")
            course_id = 'C' + str(i)
            course = Course(name, course_id)
            self.__courses_data.append(course)

    def get_grades(self):
        grades_choose = int(input("Enter the grade's ID: "))

        for student in self.__students_data:
            for course in self.__courses_data:
                if course.get_course_id() == 'C' + str(grades_choose):
                    grade = input(f"Enter {student.get_name()}'s grade for {course.get_name()}: ")
                    grade_obj = Grade(student, course, grade)
                    self.__grades_data.append(grade_obj)

    def print_grades(self):
        for grade in self.__grades_data:
            grade.display_info()


students_and_grades = StudentsAndGrades()
students_and_grades.get_students()
students_and_grades.get_courses()
students_and_grades.get_grades()
students_and_grades.print_grades()
