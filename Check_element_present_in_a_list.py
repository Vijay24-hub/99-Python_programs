#Python
#Check if the given element exits in a list
def CheckElementInList(List,strr):
    if strr in List:
        return True
    else:
        return False
strr=input("Enter any fruit names: ")
List=["apple","cherry","mango","orange","banana"]
print(List)
print("Number of fruits present in the list: ",len(List))
print(CheckElementInList(List,strr))    #Calling a function

