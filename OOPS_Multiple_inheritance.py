#Python
#Multiple Inheritance-one derived class inherits from multiple base class
class Sum:
    def add(self,a,b):
        return a+b
class Sub:
    def sub(self,a,b):
        return a-b
class Multi:
    def multi(self,a,b):
        return a*b
class Divide:
    def divide(self,a,b):
        return a/b
class derived(Sum,Sub,Multi,Divide):    #derived class
    print("The arithmetic operations are:")
myobj=derived()     #Instantiate of object
print("Addition:",myobj.add(50,70))
print("Subtraction:",myobj.sub(70,50))
print("Multiplication:",myobj.multi(10,5))
print("Division:",myobj.divide(10,5))
