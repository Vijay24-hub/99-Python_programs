#Python
#Check the given string is Symmetric or not
#The half of a string is equal to the another half
#that is symmetric
#heyhey hey==hey
def Check_Symmetric(strr):
    l=len(strr)
    if l%2!=0:
        return "The entered string is not Symmetric"
    else:
        start=0
        mid=len(strr)//2
        while start<mid and mid<l:
            if strr[start]!=strr[mid]:
                return "Not a symmetric"
            else:
                return "Symmetric"
                start+=1
                mid+=1
strr=input("Enter the String value:")
print(Check_Symmetric(strr))    #Calling a function
