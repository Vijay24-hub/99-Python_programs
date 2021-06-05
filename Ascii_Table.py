#Python
#Printing Ascii table
def ascii_table():
    print("ASCII TABLE")
    for i in range(32,65):
        print(i,"  ",chr(i))
    print()
    for j in range(65,97):
        print(j,"  ",chr(j))
    print()
    for k in range(97,128):
        print(k,"  ",chr(k))

ascii_table()   #Calling a function
