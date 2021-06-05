#Python
#Identity Operators compare the objects
#if they are equal or not equal
def Identity_Operators(x,y,z):
    print(x is y)   #returns True if both objects are same
    print(x is not z)   #returns True if both objects are not same
x=input("Give any x value:")
y=input("Give any y value:")
z=input("Give any z value:")
Identity_Operators(x,y,z)   #Calling a function
