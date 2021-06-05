#Python
#OOPs concept
#Student marklist
class student():
    def __init__(self,name,section):
        self.name=name
        self.section=section
        
    def marksheet(self,mark1,mark2,mark3):
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.sum_marks=self.mark1 + self.mark2 + self.mark3
        return mark1+mark2+mark3
        
myobj1=student("Harry","A")  #object is created
print("Student Name:",myobj1.name," of Section:",myobj1.section)
a=int(input("\nEnter maths marks: "))
b=int(input("Enter physics marks: "))
c=int(input("Enter Chemistry marks: "))

print("Total Mark:",myobj1.marksheet(a,b,c))


    
