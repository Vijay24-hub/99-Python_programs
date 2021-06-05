#Python
#Continue  statement
#when conditon is true skips the statement
def myfunc(num):
    for i in range(1,101):
        if i%num!=0:
            continue    #skip the statement
        else:
            print(i)
num=int(input("Enter the number between 1 to 100:"))
myfunc(num) #Calling a funtion
