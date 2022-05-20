class Person:
    def __init__(self,person_name, date_of_birth,height):
        self.name= person_name
        self.dof=date_of_birth
        self.ht = height

    def get_name(self):
        return self.name

    def set_name(self,new_name):
        self.name = new_name

        # if (self.has_any_number(new_name)):
        #     print("Sorry person can't have number"
            
     
    # def has_any_number(self,string):
    #     return "0" in string

    def get_summary(self):
        print (f"Name: {self.name}, DOB: {self.dof}, height: {self.ht}")

a_person = Person("Ashik",1999,5.5)   
a_person.get_summary()     

a_person.set_name("Ashik Bhuyan")  
a_person.get_summary() 


print(a_person.name)


# a_person.set_name("0")  
# a_person.get_summary() 
