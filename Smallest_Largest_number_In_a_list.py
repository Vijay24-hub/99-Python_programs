#Python
#Finding the Largest and Smallest numbers in the given list
def SmallestLargestInList(n,list1):
    list1.sort()
    print("Smallest Number in a list:",list1[0])
    print("Largest Number in a list:",list1[-1])
n=int(input("Enter the number of indexes:"))
list1=[]
print("Enter the elements:")
for i in range(n):
    element=int(input())
    list1.append(element)
print(list1)
SmallestLargestInList(n,list1)  #calling a function
