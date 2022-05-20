class Triangle :
    def __init__(self,base,height):
        self.base = base  
        self.height = height

    def calculate_area(self):  #by default self declare korthe hoi, convention
        area = 0.5 * self.base * self.height
        print("Area = ",area)



t1 = Triangle(10,20)    
t1.calculate_area()    