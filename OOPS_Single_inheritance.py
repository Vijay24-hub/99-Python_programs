#Python
#Single Inheritance-one derived class inherits from the one base class
class square:   #base class
    def __init__(self,sides):
        self.sides=sides

    def display_info(self):
        print("A Square has four equal sides")

    def get_perimeter(self):
        perimeter=4*self.sides
        return "Perimeter:{0}".format(perimeter)

    def get_area(self):
        area=self.sides**2
        return "Area:{0}".format(area)
class result(square):   #derived class
    def display_info(self):
        print("A Square has four sides")
        super().display_info()  #oject of base display_info method to print
myobj=result(5)  #Instantiate of object
print(myobj.get_perimeter())
print(myobj.get_area())
myobj.display_info()

