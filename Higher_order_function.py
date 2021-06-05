#Python
#Higher order function
#One function can be called by argument of another function 
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y

def arith(func,x,y):    #functions called by argument
    result=func(x,y)
    return result

x=int(input("Give x value:"))
y=int(input("Give y value:"))
print(arith(add,x,y))   #Calling a function
print(arith(sub,x,y))   #Calling a function
print(arith(multi,x,y)) #Calling a function
print(arith(div,x,y))   #Calling a function
