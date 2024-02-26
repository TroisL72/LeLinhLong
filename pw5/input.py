from domains.student import Student
from domains.course import Course
import numpy as np
import math

class GetInput:
    def __init__(self):
        self.students_data = []
        self.courses_data = []
        self.grades_data = []

    def get_students(self):
        num_students = int(input("Enter the number of students: "))

        with open("students.txt", "w") as file:
            for i in range(1, num_students + 1):
                name = input(f"Enter student {i}'s name: ")
                dob = input(f"Enter {name}'s date of birth: ")
                student_id = '22BI' + str(i)
                student = Student(name, dob, student_id)
                self.students_data.append(student)
                file.write(f"Name: {name}, Date of Birth: {dob}, Student ID: {student_id}\n")

    def get_courses(self):
        num_courses = int(input("Enter the number of courses: "))
    
        with open("courses.txt", "w") as file:
            for i in range(1, num_courses + 1):
                name = input(f"Enter course {i}'s name: ")
                credits = int(input(f"Enter credits for {name}: "))
                course_id = 'C' + str(i)
                course = Course(name, course_id, credits)
                self.courses_data.append(course)
                file.write(f"Course: {name}, Credits: {credits}, Course ID: {course_id}\n")

    def get_grades(self):
        with open("marks.txt", "w") as file:
            grades = [] 

            for student in self.students_data:
                student_grades = []

                for course in self.courses_data:
                    grade = float(input(f"Enter {student.get_name()}'s grade for {course.get_name()} (Course ID: {course.get_course_id()}): "))
                    grade = math.floor(grade)
                    file.write(f"{student.get_name()}, {course.get_name()}, Grade: {grade}\n")
                    student_grades.append(grade)  

                grades.append(student_grades)  

            self.grades_data = np.array(grades)

