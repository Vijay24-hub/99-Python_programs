#Python
#Finding the Even and Odd numbers in a given list
def EvenOddInList(n,list1):
    even=[]
    odd=[]
    for j in list1:
        if j%2==0:
            even.append(j)
        else:
            odd.append(j)
    print("Even list is",even)
    print("Odd list is",odd)
n=int(input("Enter the number of indexes:"))
list1=[]
for i in range(n):
    element=int(input("Enter the elements:"))
    list1.append(element)
EvenOddInList(n,list1)  #Calling a function
