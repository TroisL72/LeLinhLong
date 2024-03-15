class Course:
    def __init__(self, name, ects):
        self.name = name
        self.ects = ects

    def get_name(self):
        return self.name
    
    def get_ects(self):
        return self.ects
    
    def display_info(self):
        print(f"Course's name: {self.name}")
        print(f"Course's ECTS: {self.ects}")