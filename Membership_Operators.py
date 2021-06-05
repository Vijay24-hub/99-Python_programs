#Python
#Membership Operators test if the sequence presented in a object
def Membership_Operators(string,s):
    print(s in string)  #returns true specified value present in the object
    print(s not in string)  #returns true specified value is not present in the object
string=input("Enter a string value:")
s=input("Enter any character value:")
Membership_Operators(string,s)  #Calling a function
