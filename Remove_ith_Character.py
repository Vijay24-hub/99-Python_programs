#Python
#Removing i-th character from a string
def RemoveChar(string,i):
    newstr=""
    if i<len(string):
        fstr=string[:i]
        lstr=string[i+1:]
        newstr=fstr+lstr
        print(newstr)
    else:
        print("Enter a valid ith number less than the length of string")
string=input("Enter any string:")
i=int(input("Enter the ith number:"))
RemoveChar(string,i)    #Calling a function
