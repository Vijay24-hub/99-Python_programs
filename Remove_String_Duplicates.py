#Python
#Removing duplicates from the string
def RemoveStringDuplicates(str1):
    s1=set(str1)
    s1="".join(s1)
    print("Without order:",s1)
    t=""
    for i in str1:
        if i in t:
            pass
        else:
            t+=i
    print("With order:",t)
str1=input("Give any string value:")
RemoveStringDuplicates(str1)    #Calling a funtion

