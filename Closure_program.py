#Python
#Closue program
#Defining a Closure function
def multiples(x):   #outer enclosing function
    def multiplier(n):  #nested function
        return n*x
    return multiplier   #returns nested funtion
#try Calling the function
table2=multiples(2) 
table3=multiples(3)
table4=multiples(4)
table5=multiples(5)
print(table2(5))
print(table3(5))
print(table4(5))
print(table5(5))
#Using __closure__ attribute returns object of tuple contains
print(table2.__closure__[0].cell_contents)
print(table3.__closure__[0].cell_contents)

        
