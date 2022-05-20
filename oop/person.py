class Person:
    def __init__(self,person_name, date_of_birth,height):
        self.name= person_name
        self.dof=date_of_birth
        self.ht = height

    def set_name(self,new_name):
        self.name = new_name

    def get_summary(self):
        print (f"Name: {self.name}, DOB: {self.dof}, height: {self.ht}")

a_person = Person("Ashik",1999,5.5)   
a_person.get_summary()     

a_person.set_name("Ashik Bhuyan")  
a_person.get_summary()     
