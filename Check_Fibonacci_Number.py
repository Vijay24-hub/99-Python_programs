#Python
#Checking if the number present inside the fibonacci series
import math
def isPerfectSquare(x):
    sq=int(math.sqrt(x))
    return sq*sq==x
def isFibonacciNumber(number):
    return isPerfectSquare(5*number*number+4) or isPerfectSquare(5*number*number-4)
    if isPerfectSquare(x):  #Calling the isPerfectSquare function 
        return True         #to check the number is a perfect square number
    else:
        return False
number=int(input("Give a number:"))
print(isFibonacciNumber(number))    #Calling a function
