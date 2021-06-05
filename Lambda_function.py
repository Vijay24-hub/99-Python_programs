#Python
#Solving an experssion
#Showing difference of lambda
def myfunc(a,b):
    return (a+b)**2     #by function declaration
exp=lambda x,y:(x+y)**2 #by lambda function
print(exp(4,5)) 
print(myfunc(4,5))  #Calling a function
