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