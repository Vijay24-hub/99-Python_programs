#Python
#Raise an exception
#If condition fails raise an error and stop the execution
def myfunc(x):
    if x<0:
        raise Exception("Invalid, no Negative numbers ")
    elif x>=0 and x<18:
        print("Not eligible to vote")
    else:
        print("Eligible to vote")
x=int(input("Give any integer value:"))
myfunc(x)   #Calling a function
