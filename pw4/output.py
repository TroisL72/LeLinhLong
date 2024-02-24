from input import GetInput
import numpy as np
import math
class PrintOutput:
    def __init__(self):
        self.students_data = []
        self.courses_data = []
        self.grades_data = []
    
    def calculate_gpa(self, student_index):
        student_grades = self.grades_data[student_index]
        credits = np.array([course.get_credits() for course in self.courses_data])
        weighted_sum = np.sum(student_grades * credits)
        total_credits = np.sum(credits)
        final_gpa = math.floor(weighted_sum / total_credits)
        return final_gpa
    
    def print_grades(self):
        for student_index, student in enumerate(self.students_data):
            print(f"Student: {student.get_name()}")
            print(f"DOB: {student.get_dob()}")
            print(f"Student's ID: {student.get_student_id()}")
            print()
            for course_index, course in enumerate(self.courses_data):
                print(f"Course: {course.get_name()}")
                print(f"Course's ID: {course.get_course_id()}")
                print(f"Grade: {self.grades_data[student_index, course_index]}")
            print()

    def sort_gpa(self):
        gpa_list = [self.calculate_gpa(i) for i in range(len(self.students_data))]
        sorted_indices = np.argsort(gpa_list)[::-1]
        sorted_students = [self.students_data[i] for i in sorted_indices]
        sorted_gpas = [gpa_list[i] for i in sorted_indices]

        for student, gpa in zip(sorted_students, sorted_gpas):
            print(f"{student.get_name()}'s GPA: {gpa}")

