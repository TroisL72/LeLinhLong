from input import GetInput
from output import DataProcess
from output import PrintOutput

inp = GetInput()  
inp.get_students()
inp.get_courses()
inp.get_grades()
inp.calculate_gpa()

out = PrintOutput()
out.student_data = inp.student_data  
out.course_data = inp.course_data  
out.grade_data = inp.grade_data 
out.print_grade()

dp = DataProcess()
dp.student_data = out.student_data
dp.course_data = out.course_data
dp.grade_data = out.grade_data
dp.zipping()
dp.depickling()

