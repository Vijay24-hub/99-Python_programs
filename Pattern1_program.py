#Python
#Printing Patterns
def Pattern1(n):
    for i in range(1,n):
        for j in range(i+1):
            print("*"*j)
n=int(input("Enter a n number:"))
Pattern1(n) #Calling a function

