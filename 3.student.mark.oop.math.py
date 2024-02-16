import math
import numpy as np

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
    def __init__(self, name, course_id, credits):
        self.__name = name
        self.__course_id = course_id
        self.__credits = credits

    def get_name(self):
        return self.__name

    def get_course_id(self):
        return self.__course_id

    def get_credits(self):
        return self.__credits

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
            student_id = '22BI' + str(i)
            student = Student(name, dob, student_id)
            self.__students_data.append(student)

    def get_courses(self):
        num_courses = int(input("Enter the number of courses: "))

        for i in range(1, num_courses + 1):
            name = input(f"Enter course {i}'s name: ")
            credits = int(input(f"Enter credits for {name}: "))
            course_id = 'C' + str(i)
            course = Course(name, course_id, credits)
            self.__courses_data.append(course)

    def get_grades(self):
        grades = []

        for student in self.__students_data:
            student_grades = []

            for course in self.__courses_data:
                grade = float(input(f"Enter {student.get_name()}'s grade for {course.get_name()} (Course ID: {course.get_course_id()}): "))
                grade = math.floor(grade)
                student_grades.append(grade)

            grades.append(student_grades)

        self.__grades_data = np.array(grades)

    def calculate_gpa(self, student_index):
        student_grades = self.__grades_data[student_index]
        credits = np.array([course.get_credits() for course in self.__courses_data])
        weighted_sum = np.sum(student_grades * credits)
        total_credits = np.sum(credits)
        final_gpa = math.floor(weighted_sum / total_credits)
        return final_gpa

    def print_grades(self):
        for student_index, student in enumerate(self.__students_data):
            print(f"Student: {student.get_name()}")
            print(f"DOB: {student.get_dob()}")
            print(f"Student's ID: {student.get_student_id()}")
            print()
            for course_index, course in enumerate(self.__courses_data):
                print(f"Course: {course.get_name()}")
                print(f"Course's ID: {course.get_course_id()}")
                print(f"Grade: {self.__grades_data[student_index, course_index]}")
            print()

    def sort_gpa(self):
        gpa_list = [self.calculate_gpa(i) for i in range(len(self.__students_data))]
        sorted_indices = np.argsort(gpa_list)[::-1]
        sorted_students = [self.__students_data[i] for i in sorted_indices]
        sorted_gpas = [gpa_list[i] for i in sorted_indices]

        for student, gpa in zip(sorted_students, sorted_gpas):
            print(f"{student.get_name()}'s GPA: {gpa}")


students_and_grades = StudentsAndGrades()
students_and_grades.get_students()
students_and_grades.get_courses()
students_and_grades.get_grades()
students_and_grades.print_grades()
print("Students' list:")
students_and_grades.sort_gpa()