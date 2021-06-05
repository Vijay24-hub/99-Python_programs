#Python
#Finding the factorial of a given number
def find_factorial_number(number):
    return 1 if number==0 or number==1 else number*find_factorial_number(number-1)
number=int(input("Give a number to find the factorial number:"))
print(find_factorial_number(number))    #Calling a function
