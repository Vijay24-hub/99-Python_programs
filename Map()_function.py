#Python
#map() function
#iterates through all the items in the given iterable
#executes the function declared in the argument
#returns True or false
def map_func(list1):
    return "e" in list1            
list1=["orange","red","yellow","black","blue","green"]
map_object=map(map_func,list1) #map function
print(list(map_object))
