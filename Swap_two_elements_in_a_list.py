#Python
#Swapping the entered index number in a list
def swap_elements(n,list1,pos1,pos2):
    list1[pos1],list1[pos2]=list1[pos2],list1[pos1]
    print("After Swapping:",list1)
n=int(input("Enter the number of indexes:"))
print("Enter less than {0} positional values:".format(n))
pos1=int(input("Enter the position1:"))
pos2=int(input("Enter the position2:"))
list1=[]
for i in range(n):
    element=int(input("Enter the elements:"))
    list1.append(element)
print("Before Swapping:",list1)
swap_elements(n,list1,pos1,pos2)    #Calling a function

