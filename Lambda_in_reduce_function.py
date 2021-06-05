#Python
#lambda in reduce
from functools import reduce
list1=[23,56,76,35,22,89,32]
print(reduce(lambda x,y:x+y,list1)) #reduce with argument of lambda epression and list1
print(reduce(lambda x,y:x+y,list1,100)) #adding 100 to the expression by reduce
