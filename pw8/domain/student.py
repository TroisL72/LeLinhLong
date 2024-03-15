class Student:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def display_info(self):
        print(f"Student's name: {self.name}")