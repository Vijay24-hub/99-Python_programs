#Python
#List of Methods in List
def myfunc(list1):
    list1.append("Brown")
    print("Append:",list1)
    print("Count:",list1.count("Blue"))
    x=["Pink","Yellow"]
    list1.extend(x)
    print("Extend:",list1)
    print("Index:",list1.index("Black"))
    list1.reverse()
    print("Reverse:",list1)
    list1.sort()
    print("Sort:",list1)
    list2=list1.copy()
    print("Copy:",list2)
    list1.clear()
    print("Clear:",list1)
list1=["Black","Blue","Green","Red","Orange"]
myfunc(list1)   #Calling a function
