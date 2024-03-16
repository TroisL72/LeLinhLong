from input import GetInput
import pickle as pk
import os
import zipfile
import threading

class PrintOutput:
    def __init__(self):
        self.student_data = []
        self.course_data = []
        self.grade_data = []

    def print_grade(self):
        for i in self.grade_data:
            i.display_info()

class DataProcess:
    def zipping(self):
        try:
            with zipfile.ZipFile('students.zip','w') as z:
                z.write('students.pkl')
                z.write('courses.pkl')
                z.write('grades.pkl')
        except Exception as e:
            print(str(e))

    def depickling(self):
        if os.path.exists("students.zip"):
            try:
                with zipfile.ZipFile('students.zip', 'r') as unz:
                    unz.extractall()
            except Exception as e:
                print(str(e))
            print("File students.zip does exist")
        else: 
            print("Does not exist")
        with open("students.pkl", "rb") as file:
            self.student_data = pk.load(file)
        with open("courses.pkl", "rb") as file:
            self.course_data = pk.load(file)
        with open("grades.pkl", "rb") as file:
            self.grade_data = pk.load(file)

    def threads(self):
        t1 = threading.Thread(target=self.zipping, arg=())
        t1.start()
        t2 = threading.Thread(target=self.depickling, args=())
        t2.start()
        t1.join()
        t2.join()


        






    

