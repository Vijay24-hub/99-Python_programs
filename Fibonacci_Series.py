#Python
#Finding the fibocci series
#Till the entered number
def fibonacci_series(num):
    a,b=0,1
    print("Fibonacci series:")
    while num>0:
        print(a)
        c=a+b
        a=b
        b=c
        num-=1
num=int(input("Enter any number:"))
fibonacci_series(num)   #Calling a function
