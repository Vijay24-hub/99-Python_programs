#Python
#Transpose a given matrix 3*4-->4*3
def myfunc(matrix1):
    new_matrix=[[matrix1[i][j] for i in range(len(matrix1))] for j in range(len(matrix1[0]))]
    print("After Transpose:")
    for k in new_matrix:
        print(k)
matrix1=[[2,4,31,5],[8,99,34,75],[32,23,45,54]]
print("Before Transpose:")
for r in matrix1:
    print(r)
myfunc(matrix1)     #Calling a function
