#Python
#Changeable
#Duplicates are not allowed
def myfunc(dict1):
    dict1.update({"D":"Dog"})
    dict1["E"]="Elephant"
    dict1["B"]="Bat"
    print("\nNew dictionary",dict1)
    print("\nKeys:")
    for i in dict1.keys():
        print(i)
    print("\nValues:")
    for j in dict1.values():
        print(j)
    print("\nItems:")
    for k in dict1.items():
        print(k)
dict1={"A":"Apple",
       "B":"Ball",
       "C":"Cat"}
myfunc(dict1)   #Calling a function
