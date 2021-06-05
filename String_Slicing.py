#Python
#Return the specified number of indexes in a String
def StringSlicing(string):
    print("by start and end index:",string[6:9])    
    print("Slice from the start:",string[:5])
    print("Slice to the end:",string[6:])
    print("Negative indexing:",string[-5:-1])
    print("Entire string:",string[::1])
string="Hello world"
print(string)
print("String Slicing:")
StringSlicing(string)   #Calling a function
