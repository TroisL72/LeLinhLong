from input import GetInput
from output import PrintOutput
from output import DataProcessor

input_processor = GetInput()
input_processor.get_students()
input_processor.get_courses()
input_processor.get_grades()

output_processor = PrintOutput()
output_processor.students_data = input_processor.students_data  
output_processor.courses_data = input_processor.courses_data  
output_processor.grades_data = input_processor.grades_data 

output_processor.print_grades()
print("Students list:")
output_processor.sort_gpa()
print()

data_processor = DataProcessor()
print("Check compressing files: ")
data_processor.compress_files()
data_processor.check_and_load_data()