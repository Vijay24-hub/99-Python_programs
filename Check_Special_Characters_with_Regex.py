#Python
#With Regex module
#Checking Special Characters are found in a given String
import re
def CheckSpecialCharacters(string):
    res=re.compile("[`!@#$%^&*()_':?><|/\{},.;+=]")
    if res.search(string)==None:
        print("No Special characters are found")
    else:
        print("Speacial characters are found")
string=input("Enter any character string values:")
CheckSpecialCharacters(string)  #Calling a function
