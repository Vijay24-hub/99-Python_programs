#Python
#Printing 1 to 10 multiplication table of given number
def Tables(num):
    for i in range(1, 11):
       print(num, 'x', i, '=', num*i)

num=int(input("Enter any number:"))
Tables(num) #Calling a funtion
