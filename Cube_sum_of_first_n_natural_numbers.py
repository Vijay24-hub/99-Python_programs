#Python
#finding for the cube sum of first n natural numbers
def sum_cube_number(number):
    total=0
    while number>0:
        fact=1
        fact=pow(number,3)
        total+=fact
        number-=1
    return total
number=int(input("Enter the number:"))
print("cube sum of first {0} natural numbers is {1}".format(number,sum_cube_number(number)))  #Calling a function
