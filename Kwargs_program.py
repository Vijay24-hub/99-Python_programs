#Python
# **dwargs(keyword arguments)
# Passes keyworded variable in number of arguments
def myfunc(**kwargs):   #kwargs passing argument
    for key,value in kwargs.items():
        print("%s for %s" %(key,value))
myfunc(a="apple",b="ball",c="cat",d="dog",e="elephant") #Calling a function
