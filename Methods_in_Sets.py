#Python
#List of Methods in Sets
def myfunc(set1,set2):
    set1.add("Mango")   #add new item to the set
    print("Add:",set1)  #removes specified item
    set2.discard("Potato")
    print("Discard:",set2)
    print("Intersection:",set1.intersection(set2))  #return common items of both sets
    print("Issubset:",set1.issubset(set2))    #checks set1 all items exist in set2
    pop_item=set1.pop()
    print("pop:",set1)          #remove last item  
    remove_item=set2.remove("Onion")
    print("remove:",set2)       #remove specified item
    print("Union:",set1.union(set2))    #combination of both sets
    set1.clear()
    print("Clear:",set1)            #clear the specified sets
set1={"Apple","Orange","Cherry","Grapes"}
set2={"Onion","Tomato","Cherry","Potato"}
print("set1:",set1)
print("set2:",set2)
print()
myfunc(set1,set2)   #Calling a function
