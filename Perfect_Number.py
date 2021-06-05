#Python
#Checking if the number is perfect number or not
def perfect_number(num):
    flag=0
    for i in range(1,num):
        if num%i==0:
            flag+=i
            
    if flag==num:
        print("Perfect number")
    else:
        print("Not a perfect number")
num=int(input("Enter any positive integer:"))
perfect_number(num) #Calling a function
