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