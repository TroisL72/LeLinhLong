import math

class Student:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name

    def display_info(self):
        print(f"Student's name: {self._name}")

class Course:
    def __init__(self, name, ects):
        self._name = name
        self._ects = ects

    def get_name(self):
        return self._name
    
    def get_ects(self):
        return self._ects
    
    def display_info(self):
        print(f"Course's name: {self._name}")
        print(f"Course's ECTS: {self._ects}")

class Grade:
    def __init__(self, student, course, grade):
        self._student = student
        self._course = course
        self._grade = grade

    def display_info(self):
        self._student.display_info()
        self._course.display_info()
        print(f"Grade: {self._grade}")

class PrintOutput:
    def __init__(self):
        self._student_data = []
        self._course_data = []
        self._grade_data = []

    def get_students(self):
        num_students = int(input("Number of students: "))
        for i in range(num_students):
            ame = input("Enter student's name: ")
            student = Student(ame)
            self._student_data.append(student)

    def get_courses(self):
        num_courses = int(input("Number of courses: "))
        for i in range(num_courses):
            ame = input("Enter course's name: ")
            cts = int(input("Enter course's ECTS: "))
            ourse = Course(ame, cts)
            self._course_data.append(ourse)

    def get_grades(self):
        for student in self._student_data:
            for course in self._course_data:
                grade = float(input(f"Enter {student.get_name()}'s grade for {course.get_name()}: "))
                floor_grade = math.floor(grade)
                grade_obj = Grade(student, course, floor_grade)  
                self._grade_data.append(grade_obj)

    def calculate_gpa(self):
        gpa_dict = {}  
        for student in self._student_data:
            total_ects = 0
            total_sum = 0
            for grade in self._grade_data:
                if grade._student == student:
                    total_ects += grade._course.get_ects()
                    total_sum += grade._grade * grade._course.get_ects()
            if total_ects != 0:
                gpa = total_sum / total_ects
                gpa_dict[student.get_name()] = gpa  
            else:
                print(f"{student.get_name()} has no GPA.")

        sorted_gpa = sorted(gpa_dict.items(), key=lambda x: x[1], reverse=True)

        for student, gpa in sorted_gpa:
            print(f"{student} GPA: {gpa}")


    def print_grade(self):
        for i in self._grade_data:
            i.display_info()

if __name__ == '__main__':
    students_and_grades = PrintOutput()   
    students_and_grades.get_students()
    students_and_grades.get_courses()
    students_and_grades.get_grades()
    students_and_grades.print_grade()
    students_and_grades.calculate_gpa()
    
