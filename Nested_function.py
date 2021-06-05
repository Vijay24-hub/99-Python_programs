#Python
#Nested function
#Defining a function inside the function
def my_function(n):     #outer defined function
    def my_func():  #inner function
        #prints n number name in n number of times
        if n==1:
            print("one"*1)
        elif n==2:
            print("two"*2)
        elif n==3:
            print("three"*3)
        elif n==4:
            print("four"*4)
        elif n==5:
            print("five"*5)
        elif n==6:
            print("six"*6)
        elif n==7:
            print("seven"*7)
        elif n==8:
            print("eight"*8)
        elif n==9:
            print("nine"*9)
        else:
            print("Enter 1 to 9 numbers!!!")
    my_func()   #Calling a inner function
n=int(input("Enter any number between 1 to 9:"))
my_function(n)  #Calling a outer function
