class Person:
    def __init__(self,person_name: str, date_of_birth: int,height:int):
        self.__name= person_name
        self.__dof=date_of_birth
        self.__ht = height

    def get_name(self):
        return self.__name

    def set_name(self,new_name):
        self.__name = new_name

    def get_summary(self):
        print (f"Name: {self.__name}, DOB: {self.__dof}, height: {self.__ht}")

a_person = Person("Ashik",1999,5.5)   
a_person.get_summary()     

# print(a_person.__name) # not accessible  cz this is the private instance method and variable

a_person.set_name("Ashik Bhuyan")  
a_person.get_summary() 


