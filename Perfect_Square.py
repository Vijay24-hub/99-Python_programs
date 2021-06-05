#Python
#Checking if the given number is perfect square number or not
import math
def Perfectsquare(num):
    if num>0:
        sq=math.sqrt(num)
        return (sq*sq)==num
    return false
num=int(input("Enter any positive integer:"))
if Perfectsquare(num):
    print("Perfect square")
else:
    print("Not a perfect square")
Perfectsquare(num)  #Calling a function
