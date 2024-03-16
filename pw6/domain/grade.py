class Grade:
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade

    def display_info(self):
        self.student.display_info()
        self.course.display_info()
        print(f"Grade: {self.grade}")
    
