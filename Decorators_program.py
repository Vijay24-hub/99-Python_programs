#Python
#Decorators
#Decorates the function by adding attributes,methods,etc
#to the already created function
def update_func(func):
    def inner(x,y):
        print("The result of",x,"//",y,"is: ")
        if y==0:
            print("Cannot diviide by zero")
            return
        return func(x,y)
    return inner

@update_func    #ordinary_func=update_func(ordinary_func)
def ordinary_func(x,y):
    print(x//y)
x=int(input("Give x value:"))
y=int(input("Give y value:"))
ordinary_func(x,y)  #Calling a function
    
