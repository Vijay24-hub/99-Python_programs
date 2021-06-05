#Python
#Different ways of clearing the list 
def ClearList(n,list1,list2,list3):
    list1.clear()    #clear the list
    print("by clear method:",list1)
    list2*=0         #clear the list
    print("by multiply with 0 method:",list2)
    del list3[:]     #clear the list
    print("by del[:] method:",list3)
n=int(input("Enter the number of indexes:"))
list1=[]
list2=[]
list3=[]
print("Enter the elements:")
for i in range(n):
    element=int(input())
    list1.append(element)
    list2.append(element)
    list3.append(element)
print("list:",list1)
ClearList(n,list1,list2,list3)  #Calling a function
