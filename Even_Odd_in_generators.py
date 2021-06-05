#Python
#Printing Even and Odd using generators
def EvenOddGenerators(n,max):   #generators function
    while n<=max:
        if n%2==0:
            print("even:")
            yield n
        else:
            print("odd:")
            yield n
        n+=1
n=int(input("Enter the starting number:"))
max=int(input("Enter the ending number:"))
numbers=EvenOddGenerators(n,max)    #Calling a funtion
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))    #if next exits more than the max value shows an error
