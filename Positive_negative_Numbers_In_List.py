#Python
#Finding the Positive and Negative numbers
#in a given list
def PositiveNegativeInList(n,list1):
    positive=[]
    negative=[]
    for j in list1:     #Checking for Positive and negative integer
        if j>0:
            positive.append(j)
        else:
            negative.append(j)
    print("Positive Numbers in a list:",positive)
    print("Negative Numbers in a list:",negative)
n=int(input("Enter the number of indexes:"))
list1=[]
for i in range(n):
    element=int(input("Enter the elements:"))
    list1.append(element)
print(list1)
PositiveNegativeInList(n,list1) #Calling a function
