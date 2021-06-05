#Python
# break statement
#while condition exits the loop
def myfunc(num):
    for i in range(1,50):
        if i==num:
            break   #exit the loop
        else:
           print(i)
num=int(input("Enter the number between 1 to 50:"))
myfunc(num) #Calling a function

