#Python
#Logical Operators
#combine conditional statements
def Logical_Operators(x,y,z):
    def AND():
        if x>y and x<z: #returns true if both statements are true
            print(True)
        else:
            print(False)
    AND()
    def OR():
        if x>y or x<z:  #returns true if one of the statement is true
            print(True)
        else:
            print(False)
    OR()
    def NOT():          #returns true if result is false,reverse the result
        print(not(x<y))
    NOT() 
x=int(input("Enter the x value:"))
y=int(input("Enter the y value:"))
z=int(input("Enter the z value:"))
Logical_Operators(x,y,z)    #Calling a function
