#Python
#Try except
#Try block to test the block of code for errors
#except handle the error
def myfunc(list1):
    for i in list1:
        try:
            print("The value is ",i)
            sq=i**2
            break
        except:
            print("ZeroDivision error occurs...")
            print("Try next value")
            print()
        else:
            print("No error occurs")
    print("The result is ",sq)     
list1=["a","&",2]
myfunc(list1)   #Calling a function
    
