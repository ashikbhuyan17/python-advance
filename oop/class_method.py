class Student:
    roll= ""
    gpa  = ""

    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
        print(self.roll , roll)
        # print(f"Roll: {self.roll}, GPA: {self.gpa}") 
    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}") 

    print(f"Roll: {roll}, GPA: {gpa}") 



rahim = Student() 
rahim.set_value(101,3.55)   
rahim.display()