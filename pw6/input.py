from domain.student import Student
from domain.course import Course
from domain.grade import Grade
import pickle as pk

class GetInput:
    def __init__(self):
        self.student_data = []
        self.course_data = []
        self.grade_data = []

    def get_students(self):
        num_students = int(input("Number of students: "))
        try:
            with open("students.pkl", "ab+") as file:
                for i in range(num_students):
                    name = input("Enter student's name: ")
                    student = Student(name)
                    self.student_data.append(student)
                    pk.dump(student.__dict__, file)
        except IOError:
            print('Error in students data')

    def get_courses(self):
        num_courses = int(input("Number of courses: "))
        try:
            with open("courses.pkl", "ab+") as file:
                for i in range(num_courses):
                    name = input("Enter course's name: ")
                    ects = int(input("Enter course's ECTS: "))
                    course = Course(name, ects)
                    self.course_data.append(course)
                    pk.dump(course.__dict__, file)
        except IOError:
            print('Error in course data')

    def get_grades(self):
        try:
            with open("grades.pkl", "ab+") as file:
                for student in self.student_data:
                    for course in self.course_data:
                        grade = float(input(f"Enter {student.get_name()}'s grade for {course.get_name()}: "))
                        grade_obj = Grade(student, course, grade)  
                        self.grade_data.append(grade_obj)

                        pickle_data = {
                            "student_name": grade_obj.student.get_name(),
                            "course_name": grade_obj.course.get_name(),
                            "grade": grade_obj.grade
                        }
                        pk.dump(pickle_data, file)
        except IOError:
            print("Error in grades data")

    def calculate_gpa(self):
        gpa_dict = {}  
        try:
            with open("gpa.pkl", "ab+") as file:
                for student in self.student_data:
                    total_ects = 0
                    total_sum = 0
                    for grade in self.grade_data:
                        if grade.student == student:  
                            total_ects += grade.course.get_ects()
                            total_sum += grade.grade * grade.course.get_ects()
                    if total_ects != 0:
                        gpa = total_sum / total_ects
                        gpa_dict[student.get_name()] = gpa  
                    else:
                        print(f"{student.get_name()} has no GPA.")

                sorted_gpa = sorted(gpa_dict.items(), key=lambda x: x[1], reverse=True)

                for student, gpa in sorted_gpa:
                    print(f"{student} GPA: {gpa}")

                pk.dump(gpa_dict, file)
        
        except IOError:
            print("Error in GPAs data")
    