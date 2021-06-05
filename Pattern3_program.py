#Python
#Printing Pattern
def Pattern3(n):
    i=1
    temp=temp2=n2=n
    while n>0 and i<temp:
        print(" "*n+"*"*i)
        n-=1
        i+=1
    while n2>0 and temp2>0:
        print(" "*(temp2+1)+"*"*n2)
        n2-=1
        temp2+=1
n=int(input("Enter the n value:"))
Pattern3(n)     #Calling a function
