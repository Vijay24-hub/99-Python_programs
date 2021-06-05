#Python
#Class and Objects
class student:  #Class
    college="Srm"
    def __init__(self,name,department,year):
        self.name=name
        self.department=department
        self.year=year
#instantiate the class
myobj=student("zam","B.sc",2)   
myobj1=student("ram","BBA",3)
print("The student is studing in {}".format(myobj.__class__.college))

print("I am {} studying {} {} year".format(myobj.name,myobj.department,myobj.year))
print("I am {} studying {} {} year".format(myobj1.name,myobj1.department,myobj1.year))
