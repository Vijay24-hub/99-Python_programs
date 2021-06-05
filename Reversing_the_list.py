#Python
#Reversing the entered list of values
def ReverseList(n,list1):
    list1.reverse()
    print("After Reversing",list1)  #reverse method
    print("After Reversing by reversed method")
    for j in reversed(list1):       #reversed method
        print(j)
n=int(input("Enter the number of indexes:"))
print("Enter the elements:")
list1=[]
for i in range(n):
    element=int(input())
    list1.append(element)
print("Before Reversing:",list1)
ReverseList(n,list1)    #Calling the function
