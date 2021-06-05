#Python
#Performing Operations like
#Addition
#Subtraction
#Multiplication
#from a given number list
def OperationsInList(n,list1):
    add=0
    sub=0
    product=1
    for i in list1:
        add+=i
        sub-=i
        product*=i
    return add,sub,product
n=int(input("Enter the number of indexes:"))
list1=[]
for i in range(n):
    element=int(input("Enter the element:"))
    list1.append(element)
print(OperationsInList(n,list1))    #Calling a function
