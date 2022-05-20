class Student:
    roll = ""
    gpa = ""


rahim = Student()
print(isinstance(rahim,Student))   
rahim.roll = 101
rahim.gpa = 3.66
print(f"Roll: {rahim.roll}, GPA: {rahim.gpa}") 


kahim = Student()
# print(isinstance(kahim,Student))   
kahim.roll = 10
kahim.gpa = 4.00
print(f"Roll: {kahim.roll}, GPA: {kahim.gpa}") 