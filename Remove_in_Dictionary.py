#Python
#Removing keys and values from the dictionary
def myfunc(dict1):
    del dict1["Batman"]     # del   
    remove_value1=dict1.pop("Spiderman","Not found")    #pop method
    remove_value2=dict1.pop("Captain america","Not found")  #pop method
    print(remove_value1)                                    
    print(remove_value2)    
    print("After removing:",str(dict1))
dict1={"Superman":"DC",
       "Batman":"DC",
       "Spiderman":"Marvel",
       "Ironman":"Marvel",
       "Aquaman":"DC"}
print("Before removing:")
print(str(dict1))
myfunc(dict1)   #Calling a function
