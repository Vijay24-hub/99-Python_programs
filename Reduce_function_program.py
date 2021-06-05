#Python
#reduce
#not a built in function ,import from functools module
from functools import reduce
def reduce_func(x,y):
    return x+y
list1=[2,6,3,8,3,9]
reduce_object=reduce(reduce_func,list1) #reduce function
print(reduce_object)
