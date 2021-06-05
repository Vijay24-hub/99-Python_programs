#Python
#Addition of Two given matrix using list comprehension
def myfunc(list1,list2):
    result=[[0,0,0],
            [0,0,0],
            [0,0,0]]
    for i in range(len(result[0])):
        for j in range(len(result[0])):
            result[i][j]=list1[i][j]+list2[i][j]
    for k in result:
        print(k)
list1=[[0,0,0],
       [0,0,0],
       [0,0,0]]
print("Enter the elements of A matrix:")
for i in range(len(list1[0])):
    for j in range(len(list1[0])):
        list1[i][j]=int(input())
list2=[[0,0,0],
       [0,0,0],
       [0,0,0]]
print("Enter the elements of B matrix:")
for i in range(len(list2[0])):
    for j in range(len(list2[0])):
        list2[i][j]=int(input())
myfunc(list1,list2)     #Calling a function

    
