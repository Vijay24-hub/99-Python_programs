#Python
#Creating class and object with methods
class student:  #class
    
    def __init__(self,name,department,year):
        self.name=name
        self.department=department
        self.year=year
    #instance method
    def subjects(self,subject1,subject2,subject3):
        return "The subjects are {0},{1},{2}".format(subject1,subject2,subject3)
    def marks(self,mark1,mark2,mark3):
        return "{0}\'s marks are {1},{2},{3} out of 100 marks".format(self.name,mark1,mark2,mark3)
myobj=student("zam","BCA",2)
print(myobj.subjects("Maths","DLF","CDC"))
print(myobj.marks("78","88","67"))
