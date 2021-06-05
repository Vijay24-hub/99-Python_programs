#Python
#Checking for the Armstrong number
def armstrong_number(number):
    total=0
    x=len(number)
    for i in number:
        fact=1
        fact=pow(int(i),x)
        total+=fact
    print(total)
    return "Is a Armstrong number " if str(total)==number else "Not a Armstrong number"   
number=input("Give a number:")
print(armstrong_number(number)) #Calling a function
        
