#Python
#Adding given tuple
#to the given list
def add_tuple(list1,n):
    tuple1=(2,3,4)
    list1.extend(tuple1)    #.extend() method
    print("After extending:",list1)
n=int(input("Enter the number of indexes:"))
list1=[]
print("Enter the elements:")
for i in range(n):
    element=int(input())
    list1.append(element)
print("Before extending:",list1)
add_tuple(list1,n)  #Calling a function
