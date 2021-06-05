#Python
#Funtion returns another function
#Volume of cylinder
import math
def my_func1(r):
    def my_func2(h):
       return "Volume of cylinder is {0}".format(math.pi*r*r*h)
    return my_func2
my_func3=my_func1(10)   #Calling one function by another funtion 
print(my_func3(5))      #Calling a another function
