#Python
#List of string methods
def StringMethods(str1,str2):
    print(str1.capitalize())    #converts first character to upper case
    print(str1.count("of"))     #number of times specified value in a value
    print(str1.center(10))        #centered string
    print(str1.swapcase())      #lower case becomes upper case , upper case becomes lower case 
    print(str1.find("string"))  #position of specified string
    print(str2.islower())       #checks all characters are lower
    print(str2.index("world"))  #position of specified string
    print(str2.strip())         #trimmed version
    print(str2.split(" "))      #split string at specified separator
    print(str2.replace("world","People"))   #repace new string to specified string
str1="List of String of Methods"
str2="Hello world welcome to Python"
#Lot more String methods are there
StringMethods(str1,str2)
    
