#Python
#Convert list of tuples into dictionary
def myfunc(list_tuple,new_dict):
    for i,j in list_tuple:
        new_dict.setdefault(i,[]).append(j)
    return new_dict
list_tuple=[("Apple","red"),("Grapes","green"),("Banana","yellow"),("Mango","yellow")]
dictionary={}
print(myfunc(list_tuple,dictionary))    #Calling a function
