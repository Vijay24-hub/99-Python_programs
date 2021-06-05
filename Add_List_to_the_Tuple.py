#Python
#Adding list of string to the tuple
def add_list(tuple1,list2):
    tuple2=list(tuple1)
    for i in list2:
        tuple2.append(i)
    print(tuple(tuple2))
tuple1=("apple","butterfly","bucati","orange")
list2=["yellow","five","fish"]
add_list(tuple1,list2)   #Calling a function
