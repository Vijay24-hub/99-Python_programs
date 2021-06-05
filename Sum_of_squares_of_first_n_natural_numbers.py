#Python
#Finding the sum of squares of n natural numbers
def sum_of_squares(number):
    total=0
    for i in range(1,number+1):
        fact=1
        fact=pow(i,2)
        total+=fact
    return total
number=int(input("Enter a number:"))
print("Sum of squares of first {0} natural numbers is".format(number),sum_of_squares(number))   #Calling a function

