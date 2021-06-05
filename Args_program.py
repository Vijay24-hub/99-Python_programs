#Python
# *args(non-keyword argument)
#Pass a variable number of arguments to a function
def my_func(s1,s2,s3,s4,s5):
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
var=("keekee","weewee","leelee","beebee","jeejee")
#assigning var as args
my_func(*var) #Calling a function
