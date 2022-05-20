class Person:
    def __init__(self,person_name: str, date_of_birth: int,height:int):
        self.name= person_name
        self.dof=date_of_birth
        self.ht = height

    def get_name(self):
        return self.__name

    def set_name(self,new_name):
        self.name = new_name


    def get_year_birth(self):
        return self.dof

    def get_summary(self):
        print (f"Name: {self.name}, DOB: {self.dof}, height: {self.ht}")



person_list = [
    Person("ashik",1990,5),
    Person("jamal",1980,5),
    Person("kamal",1995,5),
    Person("joy",2000,5),
]

for person in person_list:
    # print(person.get_summary())
    # print(person.get_year_birth())
    if person.get_year_birth() >= 1990:
        print(person.get_summary())