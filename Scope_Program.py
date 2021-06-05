#Python
#Difference of global scope and local scope
x=100   #global scope
def _scope():
    y=200   #local scope 
    global z
    z=300   #global scope 
    print("Inside a funtion:")
    print(x)
    print(y)
    print(z)
_scope()    #Calling a function
print("outside a function")
print(x)
print(z)
print(y)    #Shows an error -y declared inside the function (local scope)

