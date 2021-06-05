#Python
#generators -simple way to create an iterators
def Generators(): #generator function
    num=5

    num+=5
    yield num  #yield similar to returns
    num+=5     #yield pauses funtion , saving states ,later continues successive calls
    yield num
    num+=5
    yield num
    num+=5
    yield num

numbers=Generators()    #Calling a funtion
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

