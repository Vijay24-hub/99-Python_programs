#Python
#Creating a list of tuples
#having first element as a number
#second element as a cube of a number
def tuple_cube(list1,n):
    ans=[(j,pow(j,3)) for j in list1]
    print(ans)
n=int(input("Enter the number of indexes:"))
list1=[]
print("Enter the elements:")
for i in range(n):
    element=int(input())
    list1.append(element)
tuple_cube(list1,n) #Calling a function
