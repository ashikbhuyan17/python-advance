# special type of method jake extra vabe call dithe hoi na

class Student:
    roll= ""
    gpa  = ""


    def __init__(self, roll,gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}") 

    print(f"Roll: {roll}, GPA: {gpa}") 



rahim = Student(101,3.55)   #object  initialize
rahim.display()