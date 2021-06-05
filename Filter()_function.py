#Python
#filter similar to map
#returns the object which satisfies the condition
def filter_func(list1):
    return list1[0]=="b"    #condition
list1=["black","brown","yellow","orange","blush","blue"]
filter_object=filter(filter_func,list1) #filter() function
print(list(filter_object))
