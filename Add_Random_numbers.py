#Python
#Adding Two integers by random numbers
import random
def AddRandomNumbers(x,y):
    return int(x)+int(y)
x=random.choice("1234567890")
y=random.choice("1234567890")
print(AddRandomNumbers(x,y))    #Calling a function
